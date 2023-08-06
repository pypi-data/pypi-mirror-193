from abc import ABC, abstractmethod
from datetime import datetime
from typing import TypedDict, Union


class IntervalTriggerParams(TypedDict):
    days: int
    hours: int
    minutes: int
    seconds: int
    timezone: str
    start_date: datetime
    end_date: datetime


class CronTriggerParams(TypedDict):
    year: str
    month: str
    day: str
    week: str
    day_of_week: str
    hour: str
    minute: str
    second: str
    timezone: str
    start_date: datetime
    end_date: datetime


class DateTriggerParams(TypedDict):
    run_date: datetime
    timezone: str


class ScheduleDict(TypedDict):
    func: callable
    trigger: str
    trigger_params: Union[IntervalTriggerParams, CronTriggerParams]
    name: str
    is_enabled: bool
    max_instances: int


class SchedulesDict(TypedDict):
    global_schedules: list[ScheduleDict]
    local_schedules: list[ScheduleDict]


class SchedulesMasterBase(ABC):
    @abstractmethod
    def get_all(self) -> SchedulesDict:
        raise NotImplementedError()
