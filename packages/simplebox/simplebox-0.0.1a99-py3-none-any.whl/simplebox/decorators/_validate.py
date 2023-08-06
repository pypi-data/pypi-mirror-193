#!/usr/bin/env python
# -*- coding:utf-8 -*-
from datetime import datetime
from functools import wraps
from typing import List, Callable, Tuple, Dict, Type, Optional

from ._process import _do
from .._internal._method_helper import func_full_args
from ..classes import ForceType
from ..valid import StringValidator, CompareValidator, MemberValidator, Validator, ValidatorExecutor


class Valid(object):
    name = ForceType(str)
    compare = ForceType(CompareValidator)
    string = ForceType(StringValidator)
    contain = ForceType(MemberValidator)
    contained = ForceType(MemberValidator)
    datetime_format = ForceType(str)
    empty = ForceType(bool)
    notEmpty = ForceType(bool)
    types = ForceType(tuple)
    validators = ForceType(tuple, ValidatorExecutor)

    def __init__(self, name: str, compare: Optional[CompareValidator] = None, string: Optional[StringValidator] = None,
                 contain: Optional[MemberValidator] = None,
                 contained: Optional[MemberValidator] = None,
                 datetime_format: Optional[str] = None, empty: bool = False, notEmpty: bool = False,
                 types: tuple = None,
                 validators: tuple[Validator] or ValidatorExecutor = None):
        """
        A metadata object that validates the validity of the parameter.
        :param name: Parameter name.
        :param compare: Verify that the length of the parameter is the same as expected.
        :param string: Verify that the string of the parameter.
        :param contain: Verify that the parameter contains this option. # a in b
        :param contained: Verify that the option (iterable) contains parameters. b in a
        :param datetime_format: If the parameter is time, verifies that the time is in the specified format.
        :param empty: Verify whether the parameter is empty
        :param notEmpty: The validation parameter is not empty
        :param validators: custom validator object
        """
        self.name: str = name
        self.compare: CompareValidator = compare
        self.string: StringValidator = string
        self.contain: MemberValidator = contain
        self.contained: MemberValidator = contained
        self.datetime_format: str = datetime_format
        self.empty: bool = empty
        self.notEmpty: bool = notEmpty
        self.types: tuple[Type] = types
        if types:
            self.__types_names: List[str] = [t.__name__ for t in types]
        else:
            self.__types_names = []
        self.validators: tuple[Validator] or ValidatorExecutor = validators

    @property
    def type_names(self) -> List[str]:
        return self.__types_names


def validate(*conditions: Valid):
    """
    Parameters to the validation method/function.
    :param conditions: Validation conditions, a collection of instances of Valid
    Example:
        # 1.check name in between Jerry and Tom
        class Person:

            @validate(Valid(name="name", contained=MemberValidator(in_=["Jerry", "Tom"])))
            def __init__(self, age, name):
                self.age = age
                self.name = name


        tom = Person(10, "Tom")
        tom = Person(10, "Jack") # raise exception

        # 2.check age between 1 and 10(contains 1 and 10)
        class Person:

            @validate(Valid(name="name", compare=CompareValidator(le=10, ge=1)))
            def __init__(self, age, name):
                self.age = age
                self.name = name


        tony = Person(5, "Tony")
        tony = Person(-1, "Tony")  # raise exception
    """

    def __inner(func):
        @wraps(func)
        def __wrapper(*args, **kwargs):
            opts = {"conditions": conditions, "stacklevel": 7}
            return _do(func=func, decorator_name=validate.__name__, args=args, kwargs=kwargs, opts=opts)

        return __wrapper

    return __inner


def __do_validate(func: Callable, args: Tuple = None, kwargs: Dict = None, opts: Dict = None):
    conditions: List[Valid] = opts.get("conditions", [])
    args_ = () if args is None else args
    kwargs_ = {} if kwargs is None else kwargs
    func_parameters = func_full_args(func, args_, kwargs_)
    for valid in conditions:
        if not isinstance(valid, Valid):
            raise TypeError(f"valid check metadata type error , excepted type '{Valid.__name__}', "
                            f"got a '{type(valid).__name__}'")
        parameter = func_parameters.get(valid.name)
        if valid.empty:
            assert not parameter, f"valid check parameter is empty, but '{valid.name}=({parameter})' is not empty."
        if valid.notEmpty:
            assert parameter, f"valid check parameter is not empty, but '{valid.name}=({parameter})' is empty."
        if valid.types is not None:
            type_ = type(parameter)
            assert issubclass(type_, valid.types), f"valid check parameter type, expected '{valid.type_names}', " \
                                                   f"got '{type_.__name__}'"
        if valid.compare is not None:
            valid.compare.validate(parameter)
        if valid.contain is not None:
            ori_kw = valid.contain._MemberValidator__operators
            kw = {k.name: parameter for k, v in valid.contain._MemberValidator__operators.items()}
            MemberValidator(**kw).validate(list(ori_kw.values())[0])
        if valid.contained is not None:
            valid.contained.validate(parameter)
        if valid.datetime_format is not None:
            try:
                datetime.strptime(parameter, valid.datetime_format)
                result = True
            except ValueError:
                result = False
            assert result, f"Valid datetime format check: expected datetime format '{valid.datetime_format}', " \
                           f"got '{parameter}'"
        if valid.validators is not None:
            if issubclass(type(valid.validators), tuple):
                for validator in valid.validators:
                    validator.validate(parameter)
            else:
                valid.validators.validate(parameter)


__all__ = ["validate", "Valid"]
