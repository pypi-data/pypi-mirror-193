import asyncio
import threading
from asyncio import get_running_loop
from concurrent.futures import Executor
from typing import Callable, Optional, Union

from apscheduler.schedulers.asyncio import AsyncIOScheduler as BaseAsyncScheduler
from apscheduler.util import get_callable_name, obj_to_ref, ref_to_obj, undefined
from dependency_injector.wiring import Provide, inject

from dropland.app.application import current_application
from dropland.util import invoke_sync, invoke_async, import_path
from .remote import RemoteScheduler


class Scheduler(BaseAsyncScheduler):
    def __init__(self, remote: Optional[RemoteScheduler] = None,
                 executor: Optional[Executor] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._remote = remote
        self._executor = executor
        self._lock = threading.Lock()
        self._counter = 0
        self._thread = None

    @property
    @inject
    def _inside_worker(self, _inside_worker: bool = Provide['as_service']) -> bool:
        return _inside_worker

    def _run(self):
        try:
            self._eventloop.run_forever()
        finally:
            self._eventloop.run_until_complete(self._eventloop.shutdown_asyncgens())
            self._eventloop.run_until_complete(self._eventloop.shutdown_default_executor())
            self._eventloop.close()
            self._eventloop = None

    def _start(self, paused: bool):
        if not self._eventloop:
            try:
                self._eventloop = asyncio.get_running_loop()
            except RuntimeError:
                self._eventloop = asyncio.new_event_loop()

            self._eventloop.set_default_executor(self._executor)

        if not self._eventloop.is_running() and not self._thread:
            self._thread = threading.Thread(target=self._run, name='TaskWorkerAsync')

        if self._thread and not self._thread.is_alive():
            self._thread.start()

        if self._remote and not self._inside_worker:
            self._remote.start(paused)
        else:
            super().start(paused)

    def _shutdown(self, wait: bool):
        if self._remote and not self._inside_worker:
            self._remote.shutdown(wait)
        else:
            super().shutdown(wait)

        if self._thread:
            self._eventloop.call_soon_threadsafe(self._eventloop.stop)
            self._thread.join()
            self._thread = None

        self._eventloop = None

    def start(self, paused: bool = False):
        with self._lock:
            if 0 == self._counter:
                self._start(paused)
            self._counter += 1

    def shutdown(self, wait: bool = True):
        with self._lock:
            if 1 == self._counter:
                self._shutdown(wait)
            self._counter = max(self._counter - 1, 0)

    def pause(self):
        if self._remote and not self._inside_worker:
            self._remote.pause()
        else:
            super().pause()

    def resume(self):
        if self._remote and not self._inside_worker:
            self._remote.resume()
        else:
            super().resume()

    def add_job(self, func: Union[str, Callable], trigger=None, args=None, kwargs=None, id=None, name=None,
                misfire_grace_time=undefined, coalesce=undefined, max_instances=undefined,
                next_run_time=undefined, jobstore='default', executor='default',
                replace_existing=False, **trigger_args):
        if self._remote and not self._inside_worker:
            method = self._remote.add_job
            target = func
            fname = name or get_callable_name(func)
        else:
            func = func if isinstance(func, Callable) else ref_to_obj(func)
            app = current_application()
            app_path = app.path if hasattr(app, 'path') else app.__module__
            target = Scheduler._process_entrypoint if 'process' == executor else Scheduler._local_entrypoint
            args = (app_path, obj_to_ref(func), *(args or tuple()))
            fname = name or get_callable_name(func)

            method = super().add_job

        return method(
            target, trigger, args, kwargs, id, fname, misfire_grace_time, coalesce,
            max_instances, next_run_time, jobstore, executor, replace_existing, **trigger_args)

    def scheduled_job(self, trigger, args=None, kwargs=None, id=None, name=None,
                      misfire_grace_time=undefined, coalesce=undefined, max_instances=undefined,
                      next_run_time=undefined, jobstore='default', executor='default', **trigger_args):
        return super().scheduled_job(
            trigger, args, kwargs, id, name, misfire_grace_time, coalesce,
            max_instances, next_run_time, jobstore, executor, **trigger_args)

    def modify_job(self, job_id, jobstore=None, **changes) -> bool:
        if _ := super().get_job(job_id, jobstore):
            super().modify_job(job_id, jobstore, **changes)
            return True
        if self._remote and not self._inside_worker:
            return self._remote.modify_job(job_id, jobstore, **changes)
        return False

    def reschedule_job(self, job_id, jobstore=None, trigger=None, **trigger_args) -> bool:
        if super().reschedule_job(job_id, jobstore, trigger, **trigger_args):
            return True
        if self._remote and not self._inside_worker:
            return self._remote.reschedule_job(job_id, jobstore, trigger, **trigger_args)
        return False

    def pause_job(self, job_id, jobstore=None) -> bool:
        if _ := super().get_job(job_id, jobstore):
            super().pause_job(job_id, jobstore)
            return True
        if self._remote and not self._inside_worker:
            return self._remote.pause_job(job_id, jobstore)
        return False

    def resume_job(self, job_id, jobstore=None) -> bool:
        if _ := super().get_job(job_id, jobstore):
            super().resume_job(job_id, jobstore)
            return True
        if self._remote and not self._inside_worker:
            return self._remote.resume_job(job_id, jobstore)
        return False

    def remove_job(self, job_id, jobstore=None) -> bool:
        if _ := super().get_job(job_id, jobstore):
            super().remove_job(job_id, jobstore)
            return True
        if self._remote and not self._inside_worker:
            return self._remote.remove_job(job_id, jobstore)
        return False

    def remove_all_jobs(self, jobstore=None):
        if self._remote and not self._inside_worker:
            self._remote.remove_all_jobs(jobstore)
        else:
            super().remove_all_jobs(jobstore)

    def get_job(self, job_id, jobstore=None):
        if job := super().get_job(job_id, jobstore):
            return job
        if self._remote and not self._inside_worker:
            return self._remote.get_job(job_id, jobstore)
        return None

    def get_jobs(self, jobstore=None, pending=None):
        if jobs := super().get_jobs(jobstore, pending):
            return jobs
        if self._remote and not self._inside_worker:
            return self._remote.get_jobs(jobstore, pending)
        return []

    def lookup_executor(self, alias: str):
        return self._executors.get(alias)

    @staticmethod
    async def _local_async_entrypoint(app: str, func: Union[str, Callable], *args, **kwargs):
        func = func if isinstance(func, Callable) else ref_to_obj(func)
        app = current_application()

        async with app.with_app_resources():
            async with app.with_app_sessions():
                await invoke_async(func, *args, **kwargs)

    @staticmethod
    async def _local_entrypoint(app: str, func: Union[str, Callable], *args, **kwargs):
        loop = get_running_loop()
        coro = Scheduler._local_async_entrypoint(app, func, *args, **kwargs)
        loop.call_soon(asyncio.ensure_future, coro)

    @staticmethod
    async def _process_async_entrypoint(app: str, func: Union[str, Callable], *args, **kwargs):
        func = func if isinstance(func, Callable) else ref_to_obj(func)
        app = import_path(app)

        async with app.with_app_resources():
            async with app.with_app_sessions():
                await invoke_async(func, *args, **kwargs)

    @staticmethod
    def _process_entrypoint(app, func: Union[str, Callable], *args, **kwargs):
        invoke_sync(Scheduler._process_async_entrypoint, app, func, *args, **kwargs)
