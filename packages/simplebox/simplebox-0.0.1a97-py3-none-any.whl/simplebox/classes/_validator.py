#!/usr/bin/env python
# -*- coding:utf-8 -*-
import operator
from abc import ABC, abstractmethod
from typing import Tuple

from ..enums import EnhanceEnum
from ..exceptions import ValidatorException


class _Symbols(EnhanceEnum):
    eq = "=="
    ne = "!="
    le = "<="
    lt = "<"
    ge = ">="
    gt = ">"
    is_ = "is"
    is_not = "is not"
    in_ = "in"
    not_in = "not in"


class Validator(ABC):
    """
    Custom validators need to inherit from Validator
    and must supply a validate() method to test various restrictions as needed.
    """

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


class ValidatorExecutor(Validator):

    def __init__(self, *validators: Validator):
        self.__validators: Tuple[Validator] = validators

    def validate(self, value):
        for validator in self.__validators:
            validator.validate(value)


class CompareValidator(Validator):
    """
    Compare operation checks
    """

    def __init__(self, eq=None, ne=None, le=None, lt=None, ge=None, gt=None):
        self.__operators = {_Symbols.eq: eq, _Symbols.ne: ne, _Symbols.lt: lt, _Symbols.le: le, _Symbols.ge: ge,
                            _Symbols.gt: gt}
        self.__operators = {k: v for k, v in self.__operators.items() if v is not None}

    def validate(self, value):
        for operate, obj in self.__operators.items():
            operate_ = f"__{operate.name}__"
            symbol = operate.value
            if not hasattr(obj, operate_) or not hasattr(value, operate_):
                raise ValidatorException(f"'{obj}' have not '{operate}' implemented.")
            if type(value) != type(obj):
                raise TypeError(f"'{type(value).__name__}' and '{type(obj).__name__}' cannot be '{symbol}'")
            result = getattr(operator, operate.name)(value, obj)
            if not result:
                raise ValidatorException(f"CompareValidator fail: excepted '{value}' {symbol} '{obj}', "
                                         f"but actual check fail.")


class IdentityValidator(Validator):
    """
    Identity validator
    """

    def __init__(self, is_=None, is_not=None):
        self.__operators = {_Symbols.is_: is_, _Symbols.is_not: is_not}
        self.__operators = {k: v for k, v in self.__operators.items() if v is not None}

    def validate(self, value):
        if _Symbols.is_ in self.__operators and _Symbols.is_not in self.__operators:
            raise ValidatorException(
                f"'{_Symbols.is_.value}' and '{_Symbols.is_not.value}' cannot exist at the same time.")
        for operate, obj in self.__operators.items():
            result = getattr(operator, operate.name)(value, obj)
            if not result:
                raise ValidatorException(f"Excepted '{value}' {operate.value} '{obj}', but check fail.")


class MemberValidator(Validator):
    """
    Member validators
    """

    def __init__(self, in_=None, not_in=None):
        self.__operators = {_Symbols.in_: in_, _Symbols.not_in: not_in}
        self.__operators = {k: v for k, v in self.__operators.items() if v is not None}

    def validate(self, value):
        if _Symbols.in_ in self.__operators and _Symbols.not_in in self.__operators:
            raise ValidatorException(f"'{_Symbols.in_.value}' and '{_Symbols.not_in.value}'"
                                     f" cannot exist at the same time.")
        for operate, obj in self.__operators.items():
            result = getattr(operator, "contains")(obj, value)
            if operate == _Symbols.not_in:
                result = not result
            if not result:
                raise ValidatorException(f"Excepted '{value}' {operate.value} '{obj}', but check fail.")


class StringValidator(Validator):
    """
    verifies that a value is a str.
    Optionally, it validates a given minimum or maximum length. It can validate a user-defined predicate as well.
    """

    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Expected {value!r} to be an str')
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(
                f'Expected {value!r} to be no smaller than {self.minsize!r}'
            )
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(
                f'Expected {value!r} to be no bigger than {self.maxsize!r}'
            )
        if self.predicate is not None and not self.predicate(value):
            raise ValueError(
                f'Expected {self.predicate} to be true for {value!r}'
            )


class TypeValidator(Validator):
    """
    verifies that a value type in types.
    """

    def __init__(self, *types: type):
        self.__types: tuple[type] = types
        self.__type_names: list[str] = []
        for t in types:
            if not isinstance(t, type):
                raise TypeError(f"Excepted 'type' object, got a '{t}'")
            self.__type_names.append(t.__name__)

    def validate(self, value):
        value_type = type(value)
        if not issubclass(value_type, self.__types):
            raise TypeError(f"Expected \"{self.__type_names}\", got a '{value_type.__name__}'")


__all__ = ["Validator", "ValidatorExecutor", "CompareValidator", "IdentityValidator", "MemberValidator",
           "StringValidator", "TypeValidator"]
