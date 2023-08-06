import functools
import logging
import traceback
import sys


class ConsoleInputCheck(object):
    """
    命令行输入检查, 输入正确返回, 错误重新输入

    Args:
        wish_type: 期望输入类型
        error_msg: 输入错误提示信息

    Attributes:
        wish_type: 期望输入类型
        error_msg: 输入错误提示信息
    """
    def __init__(self, wish_type, error_msg: str):
        self.wish_type = wish_type
        self.error_msg = error_msg

    def __call__(self, func):
        @functools.wraps(func)
        def true_return_error_reenter(*args, **kwargs):
            while True:
                input_val = func(*args, **kwargs)
                if isinstance(input_val, self.wish_type):
                    return input_val
                else:
                    if len(self.error_msg) > 0:
                        print(self.error_msg)
        return true_return_error_reenter


class TryExcept(object):
    """
    命令行输入检查, 输入正确返回, 错误重新输入

    Args:
        error_msg: 异常提示信息
        print_traceback: 打印traceback信息
        reraise: 重新 raise exception

    Attributes:
        error_msg: 期望输入类型
        reraise: 输入错误提示信息
    """

    def __init__(
            self,
            error_msg: str,
            print_traceback: bool = False,
            reraise: bool = False,
    ):
        self.reraise = reraise
        self.print_traceback = print_traceback
        self.error_msg = error_msg

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as err:
                if self.reraise:
                    raise err
                else:
                    if self.print_traceback:
                        traceback.print_exc()
                    if len(self.error_msg) > 0:
                        print(f"{self.error_msg}, 错误信息: {err}")
        return wrapper
