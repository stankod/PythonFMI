import inspect
from collections import OrderedDict

class multimethod:
    def __init__(self, function):
        self._dispatch = OrderedDict()
        self._add_function(function)
        self.__name__ = function.__name__

    def __call__(self, *args, **kwargs):
        return self.__get__(self, type(self))(*args, **kwargs)

    def __get__(self, obj, owner=None):
        if owner is None:
            owner = type(obj)
        def dispatched_function(*args, **kwargs):
            types = tuple(arg.__class__ for arg in args)
            func = self._dispatch_arg_types(types)
            if func is None:
                raise LookupError("No match found for the passed types.")
            if 'self' in inspect.getfullargspec(func).args:
                return func(obj, *args, **kwargs)
            else:
                return func(*args, **kwargs)
        return dispatched_function

    def _dispatch_arg_types(self, types):
        for args in self._dispatch:
            if len(types) == len(args):
                if all([issubclass(passed, arg) for arg, passed in zip(args, types)]):
                    return self._dispatch[args]

    def _get_function_arg_types(self, function):
        spec = inspect.getfullargspec(function)
        args = [arg for arg in spec.args if arg != 'self']
        return tuple(spec.annotations.get(arg, object) for arg in args)

    def _add_function(self, f):
        arg_types = self._get_function_arg_types(f)
        if self._dispatch.get(arg_types):
            raise LookupError("Function with same argument types already\
            exists.")
        self._dispatch[arg_types] = f

    def multimethod(self, function):
        if function.__name__ != self.__name__:
            raise NameError("Function names don't match.")
        self._add_function(function)
        return self
