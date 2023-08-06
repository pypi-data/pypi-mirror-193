# encoding:utf-8
from typing import Iterable, TypeVar, Callable, Any, List, Dict

__all__ = ['group_by']

T = TypeVar('T')


def group_by(iterable: Iterable[T], selector: Callable[[T], Any]) -> List[List[T]]:
    ret: Dict[Any, List[T]] = {}
    for item in iterable:
        key = selector(item)
        if key not in ret.keys():
            ret[key] = []
        ret[key].append(item)
    return list(ret.values())
