import inspect
from collections import OrderedDict

class multidispatch(type):
    def __new__(cls, name, bases, clsdict):
        newdict = duplicate_key_dict()
        for k, v in clsdict.items():
            if isinstance(v, list) and all([callable(el) for el in v]):
                newdict[k] = function_dispatch(*v)
            elif callable(v):
                newdict[k] = function_dispatch(v)
            else:
                newdict[k] = v
        return type.__new__(cls, name, bases, newdict)

    @classmethod
    def __prepare__(metacls, name, bases):
        return duplicate_key_dict()

class duplicate_key_dict(dict):
    def __setitem__(self, key, value):
        if key not in self:
            dict.__setitem__(self, key, value)
        elif not isinstance(dict.__getitem__(self, key), list):
            dup_list = [dict.__getitem__(self, key), value]
            dict.__setitem__(self, key, dup_list)
        else:
            dict.__getitem__(self, key).append(value)

class function_dispatch:
    def __init__(self, *functions):
        self._dispatch = OrderedDict()
        for func in functions:
            self._add_function(func)

    def __call__(self, *args, **kwargs):
        return self.__get__(self, type(self))(*args, **kwargs)

    def __get__(self, obj, owner=None):
        def dispatched_function(*args, **kwargs):
            func = self._dispatch_arg_types(tuple(arg.__class__ for arg in args))
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
        return tuple(spec.annotations.get(arg, object) for arg in spec.args if arg != 'self')

    def _add_function(self, f):
        arg_types = self._get_function_arg_types(f)
        if not self._dispatch.get(arg_types):
            self._dispatch[arg_types] = f
