# -*- coding: utf-8 -*-
from collections import OrderedDict

def groupby(func, seq):
    group_dict = {}
    for element in seq:
        group_dict.setdefault(func(element), []).append(element)
    return group_dict

def iterate(func):
    next_func = lambda _:_
    yield next_func
    composit_func = lambda function : (lambda _: func(function(_)))
    while True:
        next_func = composit_func(next_func)
        yield next_func

def zip_with(func, *iterables):
    if iterables != None:
        for elements in zip(*iterables):
            yield func(*elements)

def cache(func, cache_size):
    if cache_size <= 0:
        return func
    called = OrderedDict()
    def cached(*arg):
        if arg in called:
            return called[arg]
        while len(called) >= cache_size:
            called.popitem(last=False)
        value = func(*arg)
        called[arg] = value
        return value
    return cached