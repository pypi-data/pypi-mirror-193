# encoding:utf-8
import abc
import time
from typing import TypeVar, Generic

__all__ = ['ExpirationData']
T = TypeVar('T')


class ExpirationData(abc.ABC, Generic[T]):
    def __init__(self):
        self.data: T = None  # 数据
        self.expire_ts = None  # 过期时间戳，秒级

    def get(self) -> T:
        cur_ts = int(time.time())
        if self.data is not None and cur_ts < self.expire_ts:
            return self.data
        new_data = self.refresh()
        self.data = new_data
        return self.data

    @abc.abstractmethod
    def refresh(self) -> T:
        r"""
        需要在刷新数据的时候同时设置过期时间
        :return:
        """
        pass
