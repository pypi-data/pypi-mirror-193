import os
from dataclasses import dataclass
from datetime import timedelta
from typing import Dict, List, Mapping, Optional, Union

import pytz
from apscheduler.schedulers.base import BaseScheduler

from dropland.engines.base import EngineBackend
from dropland.engines.redis import USE_REDIS
from dropland.engines.sqla import SqlEngine
from dropland.log import logger, tr


@dataclass
class EngineConfig:
    sql_url: Union[str, SqlEngine] = None
    sql_tablename: Optional[str] = None
    sql_tableschema: Optional[str] = None
    redis_url: Optional[str] = None
    redis_job_key: Optional[str] = None

    job_coalesce: bool = False
    job_max_instances: int = 1
    job_misfire_grace_time: int = 24 * 3600

    task_host: str = '0.0.0.0'
    task_port: int = 3000
    task_processes: int = os.cpu_count()
    task_workers: int = os.cpu_count()
    task_rpc_timeout_seconds: int = 5
    task_rpc_num_connect_attempts: int = 10
    create_remote_engine: Optional[bool] = None
    timezone: str = 'UTC'


class SchedulerBackend(EngineBackend):
    def __init__(self, as_service: bool):
        self._engines: Dict[str, BaseScheduler] = dict()
        self._as_service = as_service

    @property
    def name(self) -> str:
        return 'scheduler'

    # noinspection PyMethodOverriding
    def create_engine(self, name: str, config: EngineConfig) -> BaseScheduler:
        if engine := self._engines.get(name):
            return engine

        from apscheduler.jobstores.memory import MemoryJobStore

        jobstores = {'default': MemoryJobStore()}

        if USE_REDIS and config.redis_url:
            from apscheduler.jobstores.redis import RedisJobStore
            from redis import ConnectionPool

            jobstores['redis'] = RedisJobStore(
                connection_pool=ConnectionPool.from_url(config.redis_url),
                jobs_key=f'{config.redis_job_key}.aps.jobs'
                    if isinstance(config.redis_job_key, str) else 'apscheduler.jobs',
                run_times_key=f'{config.redis_job_key}.aps.run_times'
                    if isinstance(config.redis_job_key, str) else 'apscheduler.run_times',
            )

        if config.sql_url:
            from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

            jobstores['sql'] = SQLAlchemyJobStore(
                url=config.sql_url if isinstance(config.sql_url, str) else None,
                engine=config.sql_url if not isinstance(config.sql_url, str) else None,
                metadata=config.sql_url.metadata if not isinstance(config.sql_url, str) else None,
                tablename=config.sql_tablename if config.sql_tablename else 'apscheduler_jobs',
                tableschema=config.sql_tableschema,
                engine_options={'pool_pre_ping': True},
            )

        job_defaults = {
            'coalesce': config.job_coalesce,
            'max_instances': config.job_max_instances,
            'misfire_grace_time': config.job_misfire_grace_time,
        }

        engine = self._create_engine(config, jobstores=jobstores, job_defaults=job_defaults)
        self._engines[name] = engine
        logger.info(tr('dropland.engines.scheduler.created'))
        return engine

    def get_engine(self, name: str) -> Optional[BaseScheduler]:
        return self._engines.get(name)

    def get_engine_names(self) -> List[str]:
        return list(self._engines.keys())

    def get_engines(self, names: Optional[List[str]] = None) -> Mapping[str, BaseScheduler]:
        engines = dict()

        if not names:
            names = self.get_engine_names()

        for name in names:
            if engine := self.get_engine(name):
                engines[name] = engine

        return engines

    def _create_engine(self, config: EngineConfig, **kwargs):
        from apscheduler.executors.asyncio import AsyncIOExecutor
        from apscheduler.executors.pool import ProcessPoolExecutor
        from concurrent.futures.thread import ThreadPoolExecutor as BackgroundExecutor
        from .local import Scheduler

        logger.info(tr('dropland.engines.scheduler.create.local'))

        executors = {
            'default': AsyncIOExecutor(),
            'process': ProcessPoolExecutor(config.task_processes),
        }

        if config.timezone:
            timezone = pytz.timezone(config.timezone) if isinstance(config.timezone, str) else config.timezone
        else:
            timezone = None

        create_remote_engine = config.create_remote_engine and not self._as_service
        executor = BackgroundExecutor(config.task_workers, thread_name_prefix='TaskWorker')
        scheduler = Scheduler(
            remote=self._create_remote(config) if create_remote_engine else None,
            executor=executor, executors=executors, timezone=timezone, **kwargs
        )
        return scheduler

    def _create_remote(self, config: EngineConfig):
        import apscheduler.jobstores.base
        from .remote import RemoteScheduler, register_exception

        logger.info(tr('dropland.engines.scheduler.create.remote'))

        register_exception(apscheduler.jobstores.base.JobLookupError)
        register_exception(apscheduler.jobstores.base.ConflictingIdError)
        register_exception(apscheduler.jobstores.base.TransientJobError)

        return RemoteScheduler(
            host=config.task_host, port=config.task_port,
            num_connect_attempts=config.task_rpc_num_connect_attempts,
            rpc_timeout=timedelta(seconds=config.task_rpc_timeout_seconds)
        )
