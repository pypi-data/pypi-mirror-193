# encoding:utf-8
__all__ = ['Singleton']


class Singleton:
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self, *args, **kwargs):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()

        return self._instance[self._cls]
