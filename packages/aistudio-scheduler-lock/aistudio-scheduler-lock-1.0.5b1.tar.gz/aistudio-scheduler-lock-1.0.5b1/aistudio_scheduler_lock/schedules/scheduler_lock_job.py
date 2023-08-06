import importlib
import logging
import os
import time
from copy import deepcopy
from datetime import datetime

import pytz
from apscheduler.job import Job
from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import apps
from django.conf import settings

from aistudio_scheduler_lock.locks.database_advisory_lock import DatabaseAdvisoryLock
from aistudio_scheduler_lock.locks.database_lock import DatabaseLock
from aistudio_scheduler_lock.locks.file_lock import FCNTLFileLock

from .schedules_master_base import ScheduleDict

logger = logging.getLogger(__name__)


class SchedulerLockJob:
    # Am I owner of the lock
    lock_owner = False
    lock = None
    if settings.SCHEDULER_LOCK_TYPE == "Database":
        lock = DatabaseLock(
            settings.SCHEDULER_LOCK_NAME,
            settings.SCHEDULER_LOCK_LEASE_TIME,
            settings.SCHEDULER_LOCK_RECORD_ID,
        )
    elif settings.SCHEDULER_LOCK_TYPE == "Database_Advisory":
        lock = DatabaseAdvisoryLock(
            settings.SCHEDULER_LOCK_NAME,
            settings.SCHEDULER_LOCK_LEASE_TIME,
            settings.SCHEDULER_LOCK_RECORD_ID,
        )
    elif settings.SCHEDULER_LOCK_TYPE == "File":
        lock = FCNTLFileLock(
            os.path.join(settings.LOCK_FILE_BASE_PATH, "aistudio.lock")
        )
    else:
        raise Exception(
            f"Scheduler lock type {settings.SCHEDULER_LOCK_TYPE} not supported."
        )

    jobs = {"global_schedules": [], "local_schedules": []}

    @staticmethod
    def get_schedules_master():
        schedules_class_str = settings.SCHEDULES_MASTER_CLASS
        schedules_class_listified = schedules_class_str.split(".")
        module_name = ".".join(schedules_class_listified[:-1])
        class_name = schedules_class_listified[-1]

        module = importlib.import_module(module_name)

        return getattr(module, class_name)

    @staticmethod
    def add_or_update_schedules(
        schedules_from_master: list[ScheduleDict],
        instance_schedules_list: list[Job],
        scheduler_lock_app,
    ):
        final_schedules_list = deepcopy(instance_schedules_list)

        for mj in schedules_from_master:

            if not mj.pop("is_enabled"):
                for job in final_schedules_list:
                    if job.name == mj["name"]:
                        scheduler_lock_app.scheduler.remove_job(job.id)
                        final_schedules_list.remove(job)
                        logger.debug(
                            f"removed disabled schedule: {os.getpid()} removed jobid: {job.id}, name: {job.name}"
                        )

            else:
                if mj["trigger"] == "date":
                    timezone = pytz.timezone(mj["trigger_params"]["timezone"])
                    current_datetime = datetime.now(timezone)
                    trigger_datetime = mj["trigger_params"]["run_date"].astimezone(
                        timezone
                    )

                    if current_datetime > trigger_datetime:
                        for job in final_schedules_list:
                            if job.name == mj["name"]:
                                final_schedules_list.remove(job)
                                logger.debug(
                                    f"removed completed one-time schedule: {os.getpid()} "
                                    f"removed jobid: {job.id}, name: {job.name}"
                                )
                        continue

                new_job = scheduler_lock_app.scheduler.add_job(
                    name=mj["name"],
                    func=mj["func"],
                    trigger=mj["trigger"],
                    max_instances=mj["max_instances"],
                    **mj["trigger_params"],
                )
                final_schedules_list.append(new_job)
                logger.debug(
                    f"adding schedule: {os.getpid()} added jobid: {new_job.id}, name: {new_job.name}"
                )

                for old_job in final_schedules_list:
                    if old_job.name == new_job.name and old_job.id != new_job.id:
                        if (
                            old_job.trigger != new_job.trigger
                            or old_job.max_instances != new_job.max_instances
                            or (
                                mj["trigger"] == "interval"
                                and (
                                    old_job.trigger.interval != new_job.trigger.interval
                                    or old_job.trigger.start_date
                                    != new_job.trigger.start_date
                                    or old_job.trigger.end_date
                                    != new_job.trigger.end_date
                                    or old_job.trigger.timezone
                                    != new_job.trigger.timezone
                                )
                            )
                            or (
                                mj["trigger"] == "cron"
                                and (
                                    old_job.trigger.year != new_job.trigger.year
                                    or old_job.trigger.month != new_job.trigger.month
                                    or old_job.trigger.day != new_job.trigger.day
                                    or old_job.trigger.week != new_job.trigger.week
                                    or old_job.trigger.day_of_week
                                    != new_job.trigger.day_of_week
                                    or old_job.trigger.hour != new_job.trigger.hour
                                    or old_job.trigger.minute != new_job.trigger.minute
                                    or old_job.trigger.second != new_job.trigger.second
                                    or old_job.trigger.start_date
                                    != new_job.trigger.start_date
                                    or old_job.trigger.end_date
                                    != new_job.trigger.end_date
                                    or old_job.trigger.timezone
                                    != new_job.trigger.timezone
                                )
                            )
                            or (
                                mj["trigger"] == "date"
                                and (
                                    old_job.trigger.run_date != new_job.trigger.run_date
                                    or old_job.trigger.timezone
                                    != new_job.trigger.timezone
                                )
                            )
                        ):
                            logger.debug(
                                f"updating existing schedule: {os.getpid()} "
                                f"updated jobid: {old_job.id}, name: {old_job.name}"
                            )

                            scheduler_lock_app.scheduler.reschedule_job(
                                old_job.id,
                                trigger=mj["trigger"],
                                **mj["trigger_params"],
                            )
                            scheduler_lock_app.scheduler.modify_job(
                                old_job.id, max_instances=mj["max_instances"]
                            )

                        scheduler_lock_app.scheduler.remove_job(new_job.id)
                        final_schedules_list.remove(new_job)
                        logger.debug(
                            f"removed new schedule: {os.getpid()} removed jobid: {new_job.id}, name: {new_job.name}"
                        )
                        break

        return final_schedules_list

    @classmethod
    def scheduler_lock(cls) -> None:
        """
        This is the schedule which checks whether the current instance holds
        the lock. If no other instance holds the lock, it acquires it and
        adds the global schedules to the instance's scheduler
        (scheduler_lock_app.scheduler). Local schedules, however, are added
        to the instance regardless of whether it holds the lock or not.
        The interval it runs after is set in the SCHEDULER_LOCK_JOB_INTERVAL
        setting.
        """

        logger.debug(
            f"running scheduler_lock job, pid: {os.getpid()}, time: {time.asctime()}"
        )

        scheduler_lock_app = apps.get_app_config("aistudio_scheduler_lock")
        SchedulesMaster = cls.get_schedules_master()

        if cls.lock_owner:
            logger.debug(f"I {os.getpid()} am already a lock owner HAHA")

            if not cls.lock.renew_lease():
                logger.debug(f"Sadly, I {os.getpid()} have lost the lease.")
                for j in cls.jobs["global_schedules"]:
                    logger.debug(
                        f"removing jobs: process {os.getpid()}, removed jobid: {j.id}"
                    )

                    try:
                        scheduler_lock_app.scheduler.remove_job(j.id)
                    except Exception as e:
                        logger.exception(e)
                    else:
                        logger.debug(
                            f"removed job: process {os.getpid()}, removed jobid: {j.id}"
                        )
                cls.lock_owner = False
                cls.jobs["global_schedules"] = []

        if not cls.lock_owner and cls.lock.try_acquire_lock():
            logger.debug(f"VOILA I {os.getpid()} am the lock owner VOILA")
            cls.lock_owner = True

        if cls.lock_owner:
            logger.debug(f"Process {os.getpid()} is adding global schedules")
            cls.jobs["global_schedules"] = cls.add_or_update_schedules(
                SchedulesMaster.get_all()["global_schedules"],
                cls.jobs["global_schedules"],
                scheduler_lock_app,
            )

        logger.debug(f"Process {os.getpid()} is adding local schedules")
        cls.jobs["local_schedules"] = cls.add_or_update_schedules(
            SchedulesMaster.get_all()["local_schedules"],
            cls.jobs["local_schedules"],
            scheduler_lock_app,
        )

        logger.debug("Following jobs will be run by pid %s: %s,", os.getpid(), cls.jobs)

    @classmethod
    def can_execute_task(cls) -> bool:
        return cls.lock.can_execute_task()

    @classmethod
    def get_current_lock_owner(cls) -> str:
        return cls.lock.get_current_owner()

    @staticmethod
    def _get_next_n_run_times(n: int, job: Job):
        run_times = []

        for i in range(n):
            if i == 0:
                next_run_time = job.next_run_time
            else:
                next_run_time = job.trigger.get_next_fire_time(
                    run_times[-1], run_times[-1]
                )

            if not next_run_time:
                break

            run_times.append(next_run_time)

        return run_times

    @classmethod
    def get_next_n_run_times(
        cls, n, func, trigger, max_instances, trigger_params
    ) -> datetime:
        temp_scheduler = BackgroundScheduler()

        j = temp_scheduler.add_job(
            func=func, trigger=trigger, max_instances=max_instances, **trigger_params
        )
        temp_scheduler.start(paused=True)

        return cls._get_next_n_run_times(n, j)
