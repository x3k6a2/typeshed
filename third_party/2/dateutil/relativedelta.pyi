from typing import overload, Any, List, Optional, SupportsFloat, TypeVar, Union
from datetime import date, datetime, timedelta

__all__ = ...  # type: List[str]

_SelfT = TypeVar('_SelfT', bound=relativedelta)
_DateT = TypeVar('_DateT', date, datetime)


class weekday(object):
    def __init__(self, weekday: int, n: Optional[int]=...) -> None: ...

    def __call__(self, n: int) -> 'weekday': ...

    def __eq__(self, other) -> bool: ...

    def __repr__(self) -> str: ...

    weekday = ...  # type: int
    n = ...  # type: int

MO = ...  # type: weekday
TU = ...  # type: weekday
WE = ...  # type: weekday
TH = ...  # type: weekday
FR = ...  # type: weekday
SA = ...  # type: weekday
SU = ...  # type: weekday


class relativedelta(object):
    def __init__(self,
                 dt1: Optional[date]=...,
                 dt2: Optional[date]=...,
                 years: Optional[int]=..., months: Optional[int]=...,
                 days: Optional[int]=..., leapdays: Optional[int]=...,
                 weeks: Optional[int]=...,
                 hours: Optional[int]=..., minutes: Optional[int]=...,
                 seconds: Optional[int]=..., microseconds: Optional[int]=...,
                 year: Optional[int]=..., month: Optional[int]=...,
                 day: Optional[int]=...,
                 weekday: Optional[Union[int, weekday]]=...,
                 yearday: Optional[int]=...,
                 nlyearday: Optional[int]=...,
                 hour: Optional[int]=..., minute: Optional[int]=...,
                 second: Optional[int]=...,
                 microsecond: Optional[int]=...) -> None: ...

    @property
    def weeks(self) -> int: ...

    @weeks.setter
    def weeks(self, value: int) -> None: ...

    def normalized(self: _SelfT) -> _SelfT: ...

    @overload
    def __add__(self: _SelfT, other: relativedelta) -> _SelfT: ...
    @overload
    def __add__(self: _SelfT, other: timedelta) -> _SelfT: ...
    @overload
    def __add__(self, other: _DateT) -> _DateT: ...
    @overload
    def __radd__(self: _SelfT, other: timedelta) -> _SelfT: ...
    @overload
    def __radd__(self, other: _DateT) -> _DateT: ...
    @overload
    def __rsub__(self: _SelfT, other: timedelta) -> _SelfT: ...
    @overload
    def __rsub__(self, other: _DateT) -> _DateT: ...
    def __sub__(self: _SelfT, other: relativedelta) -> _SelfT: ...

    def __neg__(self: _SelfT) -> _SelfT: ...

    def __bool__(self) -> bool: ...

    def __nonzero__(self) -> bool: ...

    def __mul__(self: _SelfT, other: SupportsFloat) -> _SelfT: ...

    def __rmul__(self: _SelfT, other: SupportsFloat) -> _SelfT: ...

    def __eq__(self, other) -> bool: ...

    def __ne__(self, other: object) -> bool: ...

    def __div__(self: _SelfT, other: SupportsFloat) -> _SelfT: ...

    def __truediv__(self: _SelfT, other: SupportsFloat) -> _SelfT: ...

    def __repr__(self) -> str: ...
