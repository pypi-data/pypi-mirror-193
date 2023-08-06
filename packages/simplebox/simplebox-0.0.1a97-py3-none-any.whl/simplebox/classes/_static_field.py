#!/usr/bin/env python
# -*- coding:utf-8 -*-
from types import GenericAlias
from typing import Tuple, Type, _Final


class ForceType(object):
    """
    Given a type as the type of a variable, an exception is thrown if the assigned type is inconsistent with that type.

    Excample:
        class Person:
            age = ForceType(int) # ForceType(int, bool)
            name = ForceType(str)

            def __init__(self, age, name):
                self.age = age
                self.name = name

        tony = Person(15, 'Tony')
        tony.age = '15'  # raise exception
    """

    def __init__(self, *types: Type):
        for t in types:
            if not issubclass(type(t), (type, _Final, GenericAlias)):
                raise TypeError(f"expected 'type' type class, but found '{type(t).__name__}'")
        self.__types: Tuple[Type] = types
        self._types_str = [i.__name__ for i in self.__types]

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set_name__(self, cls, name):
        self.name = name

    def __set__(self, instance, value):
        if value is not None:
            value_type = type(value)
            if not issubclass(value_type, self.__types):
                raise TypeError(f"expected {self._types_str}, got '{value_type.__name__}'")
        instance.__dict__[self.name] = value


__all__ = [ForceType]
