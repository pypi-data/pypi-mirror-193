#!/usr/bin/env python
# encoding: utf-8
__author__ = 'l9h8'
__time__ = '2020/9/3 4:41 PM'


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


__all__ = ["Singleton"]
