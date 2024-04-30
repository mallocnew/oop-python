#!/usr/bin/env python3
#
# Author : easytojoin@163.com (Jok)
# Date   : Tue Apr 30 11:27:09 CST 2024
#

from typing import Any


class SingletonMeta(type):
    _instance = {}
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwds)
            cls._instance[cls] = instance
        return cls._instance[cls]

class Singleton(metaclass = SingletonMeta):
    def show_myself(self):
        print(f"id of myself: {id(self)}")

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    s1.show_myself()
    s2.show_myself()
    assert(id(s1)==id(s2))
    print(f"s1: {id(s1)}, s2: {id(s2)}")
    exit(0)
