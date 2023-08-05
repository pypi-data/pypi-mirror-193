from __future__ import annotations
import pathlib
from functools import wraps
import string
from typing import Callable
from .parsing import parameterize, amend_args
from .style import TerminalStyle
from os import path
from os.path import exists


@parameterize
def validate_evenly_divisible(function: Callable, numerator=0, denominator=1, axis=1):
    """
    Decorator for validating existence of paths

    :param function: function to be decorated
    :type function: Callable
    :param numerator: position of numerator for division
    :type numerator: int
    :param denominator: position of denominator for division
    :type denominator: int
    :param axis: axis of numerator to divide
    :type axis: int
    """
    @wraps(function)
    def decorator(*args, **kwargs):
        numerator_val = args[numerator]
        denominator_val = args[denominator]

        if numerator_val.shape[axis] // denominator_val != numerator_val.shape[axis] / denominator_val:
            raise AssertionError(f"{TerminalStyle.GREEN}Not Evenly Divisible: "
                                 f"{TerminalStyle.BLUE}{numerator_val.shape[axis]}{TerminalStyle.YELLOW}"
                                 f"not evenly divisible by {TerminalStyle.BLUE}{denominator_val} "
                                 f"{TerminalStyle.RESET}")
        # noinspection PyArgumentList
        return function(*args, **kwargs)
    return decorator


@parameterize
def validate_exists(function: Callable, pos: int = 0) -> Callable:
    """
    Decorator for validating existence of paths

    :param function: function to be decorated
    :type function: Callable
    :param pos: index of the argument to be validated
    :type pos: int
    """
    @wraps(function)
    def decorator(*args, **kwargs):
        string_input = str(args[pos])
        if not exists(string_input):
            raise FileNotFoundError(f"{TerminalStyle.GREEN}Invalid Path: "
                                    f"{TerminalStyle.YELLOW} could not locate the given path"
                                    f"{TerminalStyle.BLUE}{string_input} {TerminalStyle.RESET}")
        # noinspection PyArgumentList
        return function(*args, **kwargs)
    return decorator


@parameterize
def validate_extension(function: Callable, required_extension: str, pos: int = 0) -> Callable:
    """
    Decorator for validating extension requirements

    :param function: function to be decorated
    :type function: Callable
    :param required_extension: required extension
    :type required_extension: str
    :param pos: index of the argument to be validated
    :type pos: int
    """
    @wraps(function)
    def decorator(*args, **kwargs):
        if not pathlib.Path(args[pos]).suffix:
            args = amend_args(args,  "".join([str(args[pos]), required_extension]), pos)
        if pathlib.Path(args[pos]).suffix != required_extension:
            raise ValueError(f"{TerminalStyle.GREEN}Input {pos}: {TerminalStyle.YELLOW}"
                             f"filepath must contain the required extension {TerminalStyle.BLUE}"
                             f"{required_extension} {TerminalStyle.RESET}")
        # noinspection PyArgumentList
        return function(*args, **kwargs)
    return decorator


@parameterize
def validate_filename(function: Callable, pos: int = 0) -> Callable:
    """
    Decorator for validating filenames

    :param function: function to be decorated
    :type function: Callable
    :param pos: index of the argument to be validated
    :type pos: int
    """
    @wraps(function)
    def decorator(*args, **kwargs):
        string_input = str(args[pos]).split("\\")[-1]
        if not set(string_input) <= set(string.ascii_letters + string.digits + "." + "_"):
            raise ValueError(f"{TerminalStyle.GREEN}Invalid Filename: "
                             f"{TerminalStyle.YELLOW}filenames are limited to standard letters and digits only."
                             f"{TerminalStyle.RESET}")
        # noinspection PyArgumentList
        return function(*args, **kwargs)
    return decorator


@parameterize
def validate_matrix(function: Callable, pos: int = 0) -> Callable:
    """
    Decorator for validating matrices

    :param function: function to be decorated
    :type function: Callable
    :param pos: index of the argument to be validated
    :type pos: int
    """
    @wraps(function)
    def decorator(*args, **kwargs):
        var_input = args[pos]
        if len(var_input.shape) != 2:
            raise AssertionError(f"{TerminalStyle.GREEN} Input {pos}: {TerminalStyle.YELLOW}required to be in matrix "
                                 f"format {TerminalStyle.RESET}")
        # noinspection PyArgumentList
        return function(*args, **kwargs)
    return decorator


@parameterize
def validate_numpy_type(function: Callable, required_dtype: str, pos: int = 0) -> Callable:
    """
    Decorator for validating numpy types

    :param function: function to be decorated
    :type function: Callable
    :param required_dtype: required numpy type
    :type required_dtype: str
    :param pos: index of the argument to be validated
    :type pos: int
    """
    @wraps(function)
    def decorator(*args, **kwargs):
        if args[pos].dtype != required_dtype:
            raise TypeError(f"{TerminalStyle.GREEN}Input {pos} Invalid Type: "
                            f"{TerminalStyle.YELLOW}the required type is "
                            f"{TerminalStyle.BLUE}{required_dtype}{TerminalStyle.RESET}")
        # noinspection PyArgumentList
        return function(*args, **kwargs)
    return decorator


@parameterize
def validate_path(function: Callable, pos: int = 0) -> Callable:
    """
    Decorator for validating paths

    :param function: function to be decorated
    :type function: Callable
    :param pos: index of the argument to be validated
    :type pos: int
    """
    @wraps(function)
    def decorator(*args, **kwargs):
        string_input = str(args[pos])
        if [_char for _char in list(string_input) if _char in [":", "usr", "Users"]].__len__() != 1:
            raise ValueError(f"{TerminalStyle.GREEN}Invalid Path: "
                             f"{TerminalStyle.YELLOW}no root detected in the given path "
                             f"{TerminalStyle.BLUE}{string_input} "
                             f"{TerminalStyle.RESET}")
        if not set(string_input) <= set(string.ascii_letters + string.digits + "." + "/" + "\\" + ":" + "-" + "_"):
            raise ValueError(f"{TerminalStyle.GREEN}Invalid Path: "
                             f"{TerminalStyle.YELLOW}filenames are limited to standard letters, digits, backslash, "
                             f"colon, hyphen, and underscore only."
                             f"{TerminalStyle.RESET}")
        # noinspection PyArgumentList
        return function(*args, **kwargs)
    return decorator


@parameterize
def validate_range(function: Callable, r_min: float, r_max: float, pos: int = 0) -> Callable:
    """
    Decorator to validate value is within range

    :param function: function to be decorated
    :type function: Callable
    :param r_min: minimum
    :type r_min: float
    :param r_max: maximum
    :type r_max: float
    :param pos: index of the argument to be validated
    :type pos: int
    """
    @wraps(function)
    def decorator(*args, **kwargs):
        val = args[pos]

        if not r_min <= val <= r_max:
            raise ValueError(f"{TerminalStyle.GREEN}Input {pos}: {TerminalStyle.YELLOW} value "
                             f"{TerminalStyle.BLUE}{args[pos]} {TerminalStyle.YELLOW} out of range"
                             f"{TerminalStyle.BLUE}{r_min}-{r_max}{TerminalStyle.RESET}")
        # noinspection PyArgumentList
        return function(*args, **kwargs)
    return decorator


@parameterize
def validate_strong_type(function: Callable, required: type, pos: int = 0) -> Callable:
    """
    Decorator for strong typing only one argument

    :param function: function to be decorated
    :type function: Callable
    :param required: required type
    :type required: type
    :param pos: index of the argument to be validated
    :type pos: int
    """
    @wraps(function)
    def decorator(*args, **kwargs):
        var = args[pos]
        if not isinstance(var, required):
            raise AssertionError(f"{TerminalStyle.GREEN}Input {pos}:{TerminalStyle.YELLOW} must be{TerminalStyle.BLUE} "
                                 f"{required}{TerminalStyle.YELLOW} not {TerminalStyle.BLUE}{type(var)}"
                                 f"{TerminalStyle.RESET}")
        # noinspection PyArgumentList
        return function(*args, **kwargs)
    return decorator


@parameterize
def validate_tensor(function: Callable, pos: int = 0) -> Callable:
    """
    Decorator to assert argument is a tensor

    :param function: function to be decorated
    :type function: Callable
    :param pos: index of the argument to be validated
    :type pos: int
    """
    @wraps(function)
    def decorator(*args, **kwargs):
        var_input = args[pos]
        if len(var_input.shape) != 3:
            raise AssertionError(f"{TerminalStyle.GREEN} Input {pos}: {TerminalStyle.YELLOW}requires tensor format "
                                 f"{TerminalStyle.RESET}")
        # noinspection PyArgumentList
        return function(*args, **kwargs)
    return decorator
