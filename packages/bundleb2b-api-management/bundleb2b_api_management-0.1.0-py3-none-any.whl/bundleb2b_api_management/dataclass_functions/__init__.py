
from typing import Any, List, Dict, TypeVar, Type, Callable, cast
from enum import Enum
from datetime import datetime
import dateutil.parser
from dataclasses import dataclass
from typing import Optional, Any, List, Dict



T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x

def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False

def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(float(x), float)
    return float(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()

def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }

def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


@dataclass
class Pagination:
    offset: Optional[int] = None
    limit: Optional[int] = None
    total_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Pagination':
        assert isinstance(obj, dict)
        offset = from_union([from_int, from_none], obj.get("offset"))
        limit = from_union([from_int, from_none], obj.get("limit"))
        total_count = from_union([from_int, from_none], obj.get("totalCount"))
        return Pagination(offset, limit, total_count)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.offset is not None:
            result["offset"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.offset)
        if self.limit is not None:
            result["limit"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.limit)
        if self.total_count is not None:
            result["totalCount"] = from_union([from_int, from_none], self.total_count)
        return result
