#!/usr/bin/env python3
import functools


def catch_all_and_print(f):
    """A function wrapper for catching all exceptions and logging them"""

    @functools.wraps(f)
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as ex:
            print(f"EXCEPTION {ex} in {f.__name__} with args:{args}, kwargs{kwargs}")

    return inner
