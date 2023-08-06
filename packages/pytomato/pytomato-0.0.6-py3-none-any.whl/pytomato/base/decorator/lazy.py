# encoding:utf-8

__all__ = ['lazy_constant']


class LazyConstant:

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        val = self.func(instance)
        setattr(instance, self.func.__name__, val)
        return val


lazy_constant = LazyConstant
