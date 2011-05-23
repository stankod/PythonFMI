from inspect import getfullargspec as argspec

class interface(type):
    def __new__(cls, name, bases, _dict):
        cls._check_if_public(_dict)
        cls._check_if_not_method(_dict)
        methods = {k:v for k, v in _dict.items() if callable(v)}
        cls._methods_implemented(methods)
        _dict['__new__'] = cls.init_interface
        result = type.__new__(cls, name, bases, _dict)
        result.__methods = methods
        return result

    def init_interface(self, klass):
        klass_methods = [k for k, v in klass.__dict__.items() if callable(v)]
        klass_methods = sorted(klass_methods)
        intf_methods = sorted(self.__methods.keys())
        if not all([intf_m in klass_methods for intf_m in intf_methods]):
            raise AssertionError('different attributes:\nInterface:\
            {0}\nClass:\
            {1}.'.format(set(self.__methods.keys()),set(klass_methods)))
        for cls_method, intf_method in zip(klass_methods, intf_methods):
            intf_spec = argspec(self.__methods[intf_method])
            cls_spec = argspec(klass.__dict__[cls_method])
            intf_args = intf_spec.args
            cls_args = cls_spec.args

            if self.__methods[intf_method].__doc__ != None and\
                    klass.__dict__[cls_method].__doc__ == None:
                klass.__dict__[cls_method].__doc__ = self.__methods[intf_method].__doc__

            if not (cls_args == intf_args):
                raise AssertionError('different arguments:\nInterface:\
                        {0} for {1}\nClass: {2} for {3}.'.format(intf_args,
                            intf_method, cls_args, cls_method))

            if intf_spec.varargs != cls_spec.varargs:
                        raise AssertionError('varargs missing in method\
                                {0}.'.format(cls_method))

            if intf_spec.varkw != cls_spec.varkw:
                        raise AssertionError('kwargs  missing in method\
                                {0}.'.format(cls_method))

            if set(intf_spec.kwonlyargs) != set(cls_spec.kwonlyargs):
                        raise AssertionError('kwonlyargs missing in method\
                                {0}.'.format(cls_method))
        return type.__new__(type(klass), klass.__name__, klass.__bases__,\
                dict(klass.__dict__))

    def _check_if_not_method(_dict):
        if not all([callable(v) for k, v in _dict.items() if k !=
        '__module__']):
            raise AssertionError('Not all attributes are methods')

    def _check_if_public(iterable):
        def not_public(attribute):
            if attribute.startswith('_') and\
                    not ( attribute.startswith('__') and\
                    attribute.endswith('__') ):
                raise AssertionError('Not all attributes are public.')
        [not_public(attr) for attr in iterable]

    def _methods_implemented(_dict):
        for k, v in _dict.items():
            code = v.__code__.co_code
            if code != b'd\x00\x00S' and code != b'd\x01\x00S':
                raise AssertionError('Implementation in interface')
