import re
from inspect import getfullargspec as argspec

class interface(type):
    def __new__(cls, name, bases, _dict):
        [cls._assert_public_attribute(attr) for attr in _dict]
        cls._check_if_not_method(_dict)
        cls._methods_implemented([v for v in _dict.values() if callable(v)])

        _dict['__new__'] = cls.check_implementation
        return type.__new__(cls, name, bases, _dict)

    def check_implementation(self, klass):
        klass_methods = {k for k, v in klass.__dict__.items() if callable(v)}
        intf_methods = {k for k, v in self.__dict__.items() if callable(v)}

        if not ( intf_methods <= klass_methods ):
            raise AssertionError(\
                'Methods not implemented:\n{0}.'.format(set(intf_methods)-set(klass_methods)))

        for method in intf_methods:
            intf_spec = argspec(self.__dict__[method])
            cls_spec = argspec(klass.__dict__[method])

            if self.__dict__[method].__doc__ != None and\
                    klass.__dict__[method].__doc__ == None:
                klass.__dict__[method].__doc__ = self.__dict__[method].__doc__

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

    def _check_if_not_method(_dict):
        if not all([callable(v) for k, v in _dict.items() if k != '__module__']):
            raise AssertionError('Not all attributes are methods')

    def _assert_public_attribute(attribute):
        if re.match(r'^_[^_]\w*$', attribute):
            raise AssertionError('Not all attributes are public.')

    def _methods_implemented(methods):
        for method in methods:
            code = method.__code__.co_code
            if code != b'd\x00\x00S' and code != b'd\x01\x00S':
                raise AssertionError('Implementation of a method in the interface.')
