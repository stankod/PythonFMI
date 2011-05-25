import re
from types import FunctionType
from inspect import getfullargspec as argspec

class interface(type):
    def __new__(cls, name, bases, _dict):
        for attr in _dict:
            cls._assert_public_attribute(attr)
        cls._check_if_not_method(cls, _dict)
        cls._check_for_implementation([v for v in _dict.values() if callable(v)])
        _dict['__new__'] = cls.check_implementation
        return type.__new__(cls, name, bases, _dict)

    def check_implementation(self, klass):
        klass_methods = {k for k, v in klass.__dict__.items() if callable(v)}
        intf_methods = {k for k, v in self.__dict__.items() if callable(v)}
        #klass_methods = set(interface._get_system_attributes(klass)[0])
        #intf_methods = set(interface._get_system_attributes(self)[0])
        if not intf_methods <= klass_methods:
            raise AssertionError(\
                'Methods not implemented:\n{0}.'.format(set(intf_methods)-set(klass_methods)))

        for method in intf_methods:
            intf_spec = argspec(self.__dict__[method])
            cls_spec = argspec(klass.__dict__[method])
            #intf_spec = argspec(self.__getattribute__(self, method))
            #cls_spec = argspec(klass.__getattribute__(klass, method))

            if klass.__dict__[method].__doc__ is None:
                klass.__dict__[method].__doc__ = self.__dict__[method].__doc__
            #if klass.__getattribute__(klass, method).__doc__ is None:
            #    klass.__getattribute__(klass, method).__doc__ = \
                    #            self.__getattribute__(self, method).__doc__

            if not (cls_spec.args == intf_spec.args):
                raise AssertionError('Different arguments:\nInterface:\
                        {0} for {1}\nClass: {2} for {3}.'.format(intf_spec.args,
                            method, cls_spec.args, method))

            if intf_spec.varargs != cls_spec.varargs:
                        raise AssertionError('varargs missing in method {0}.'.format(method))

            if intf_spec.varkw != cls_spec.varkw:
                        raise AssertionError('kwargs  missing in method {0}.'.format(method))

            if set(intf_spec.kwonlyargs) != set(cls_spec.kwonlyargs):
                        raise AssertionError('kwonlyargs missing in method {0}.'.format(method))

        return type.__new__(type(klass), klass.__name__, klass.__bases__, dict(klass.__dict__))

    def _get_system_attributes(cls):
        callables, notcallables = [], []
        for attr in dir(cls):
            if not isinstance(cls.__getattribute__(cls, attr), FunctionType):
                notcallables.append(attr)
            else:
                callables.append(attr)
        return callables, notcallables

    def _check_if_not_method(self, _dict):
        nonmethod_exceptions = self._get_system_attributes(type('a', (object,), {}))[1]
        if not all([callable(v) for k, v in _dict.items() if k not in\
            nonmethod_exceptions]):
            raise AssertionError('Not all attributes are methods')

    def _assert_public_attribute(attribute):
        if re.match(r'^_[^_]\w*$', attribute):
            raise AssertionError('Not all attributes are public.')

    def _check_for_implementation(methods):
        for method in methods:
            code = method.__code__.co_code
            consts = method.__code__.co_consts
            if code != b'd\x00\x00S':
                if code != b'd\x01\x00S':
                    raise AssertionError('Implementation of a method in the interface.')
                elif len(consts) > 2 or consts[1] != None:
                    raise AssertionError('Implementation of a method in the interface.')
