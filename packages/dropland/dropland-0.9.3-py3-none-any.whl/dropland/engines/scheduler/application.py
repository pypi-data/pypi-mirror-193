from datetime import datetime
from typing import Mapping, Optional, Union

import rpyc
from apscheduler.schedulers.base import STATE_STOPPED
from apscheduler.util import undefined
from dependency_injector import containers
from dependency_injector.containers import Container
from dependency_injector.wiring import Provide, inject

from dropland.app.application import Application
from dropland.app.base import ModuleFactory, ResourceFactory, ServiceFactory
from dropland.engines.scheduler.containers import SchedulerResource, SimpleSchedulerContainer
from dropland.log import tr, worker_logger
from .engine import EngineConfig
from .local import Scheduler


class SchedulerRPC(rpyc.Service):
    def __init__(self, scheduler: Scheduler):
        self._scheduler = scheduler

    def _prepare_args(self, args: tuple) -> tuple:
        result = []
        for value in args:
            if isinstance(value, datetime):
                value = value.strftime('%Y-%m-%dT%H:%M:%S.%f')
            elif isinstance(value, type(undefined)):
                value = undefined
            result.append(value)
        return tuple(result)

    def _prepare_kwargs(self, args: dict) -> dict:
        for k, v in args.items():
            if isinstance(v, datetime):
                args[k] = v.strftime('%Y-%m-%dT%H:%M:%S.%f')
            elif isinstance(v, type(undefined)):
                args[k] = undefined
        return args

    def exposed_start(self, paused=False):
        return self._scheduler.start(paused)

    def exposed_shutdown(self, wait=True):
        return self._scheduler.shutdown(wait)

    def exposed_pause(self):
        return self._scheduler.pause()

    def exposed_resume(self):
        return self._scheduler.resume()

    def exposed_add_job(self, func, *args, **kwargs):
        return self._scheduler.add_job(func, *self._prepare_args(args), **self._prepare_kwargs(kwargs))

    def exposed_scheduled_job(self, trigger, *args, **kwargs):
        return self._scheduler.scheduled_job(trigger, *args, **kwargs)

    def exposed_modify_job(self, job_id, jobstore=None, **changes):
        if _ := self._scheduler.get_job(job_id, jobstore):
            self._scheduler.modify_job(job_id, jobstore, **changes)
            return True
        return False

    def exposed_reschedule_job(self, job_id, jobstore=None, trigger=None, **trigger_args):
        return self._scheduler.reschedule_job(job_id, jobstore, trigger, **trigger_args)

    def exposed_pause_job(self, job_id, jobstore=None):
        return self._scheduler.pause_job(job_id, jobstore)

    def exposed_resume_job(self, job_id, jobstore=None):
        return self._scheduler.resume_job(job_id, jobstore)

    def exposed_remove_job(self, job_id, jobstore=None):
        return self._scheduler.remove_job(job_id, jobstore)

    def exposed_remove_all_jobs(self, jobstore=None):
        return self._scheduler.remove_all_jobs(jobstore)

    def exposed_get_job(self, job_id, jobstore=None):
        return self._scheduler.get_job(job_id, jobstore)

    def exposed_get_jobs(self, jobstore=None, pending=None):
        return self._scheduler.get_jobs(jobstore, pending)

    @property
    def exposed_running(self):
        return self._scheduler.running


class SchedulerApplication(Application):
    def __init__(self, container: Container, name: str,
                 engine_config: Union[EngineConfig, dict],
                 scheduler_block_name: str = 'scheduler',
                 resources: Optional[Mapping[str, ResourceFactory]] = None,
                 services: Optional[Mapping[str, ServiceFactory]] = None,
                 modules: Optional[Mapping[str, ModuleFactory]] = None):
        super().__init__(container, name, resources=resources, services=services, modules=modules)

        scheduler_resource: SchedulerResource = self.get_resource(scheduler_block_name)
        scheduler_resource.container.as_service.override(True)
        scheduler_resource.container.reset_singletons()

        self._scheduler = scheduler_resource.get_instance()
        self._engine_config = engine_config

    @property
    def scheduler(self):
        return self._scheduler

    def _create_server(self, engine_config: Union[EngineConfig, dict]):
        from rpyc.utils.server import ThreadPoolServer

        worker_logger.info(tr('dropland.engines.scheduler.service.start'))

        engine_config = engine_config if isinstance(engine_config, EngineConfig) else EngineConfig(**engine_config)

        config = rpyc.core.protocol.DEFAULT_CONFIG.copy()
        config.update({'allow_public_attrs': True, 'allow_pickle': True, 'import_custom_exceptions': True})

        return ThreadPoolServer(
            SchedulerRPC(self._scheduler), nbThreads=engine_config.task_workers,
            hostname=engine_config.task_host, port=engine_config.task_port,
            protocol_config=config
        )

    # noinspection PyBroadException
    def run(self):
        try:
            server = self._create_server(self._engine_config)
            server.start()

        except (KeyboardInterrupt, SystemExit):
            pass
        except BaseException:
            worker_logger.exception(tr('dropland.engines.scheduler.service.exception'))
        finally:
            worker_logger.info(tr('dropland.engines.scheduler.service.stop'))
            if STATE_STOPPED != self._scheduler.state:
                self._scheduler.shutdown()


@inject
def run_service(container: SimpleSchedulerContainer = Provide['<container>']):
    """ Worker service entrypoint """
    if not isinstance(container, (SimpleSchedulerContainer, containers.DynamicContainer)):
        container = SimpleSchedulerContainer()
        application = SchedulerApplication(container, 'worker', EngineConfig())
    else:
        application = container.instance(container)

    application.run()


if __name__ == '__main__':
    run_service()
