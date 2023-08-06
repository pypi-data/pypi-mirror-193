import os
import inquirer
from .decorators import ConsoleInputCheck, TryExcept


@ConsoleInputCheck(wish_type=str, error_msg="你输入的目录不存在！！！")
def get_dir_path(prompt):
    dir_name = input(prompt).strip()
    if os.path.exists(dir_name):
        return dir_name


@ConsoleInputCheck(wish_type=str, error_msg="你输入的字符串为空！！！")
def get_str(prompt):
    trip_input = input(prompt).strip()
    if len(trip_input) > 0:
        return trip_input


@ConsoleInputCheck(wish_type=int, error_msg="")
@TryExcept(error_msg="你输入的不是整数！！！")
def get_int(prompt):
    trip_input = input(prompt).strip()
    int_val = int(trip_input)
    return int_val


@ConsoleInputCheck(wish_type=int, error_msg="")
@TryExcept(error_msg="你输入的不是整数！！！")
def get_int_range(prompt, min_num, max_num):
    """
    输入取值范围内的int值
    Args:
        prompt:
        min_num:
        max_num:

    Returns:

    """
    trip_input = input(prompt).strip()
    int_val = int(trip_input)
    if min_num <= int_val <= max_num:
        return int_val
    else:
        print(f"你输入整数超出指定范围[{min_num},{max_num}] ！！！")


def get_select_input(prompt_head, prompt_foot, choices_list):
    """
    命令行select输入: 显示选项列表，并允许选择其中一个选项 (输入选择)
    Args:
        prompt_head: 输入选项头部提示
        prompt_foot: 输入选项尾部提示
        choices_list: 输入选项列表

    Returns:

    """
    choices_dict = {str(k + 1): v for k, v in enumerate(choices_list)}
    while True:
        prompt_msg = f'\n{prompt_head}\n'
        for k, v in choices_dict.items():
            prompt_msg += f"{k}: {v}\n"
        prompt_msg += prompt_foot

        input_msg = input(prompt_msg).strip()
        if len(input_msg) <= 0:
            continue

        if input_msg in choices_dict:
            input_val = choices_dict.get(input_msg, '')
            return input_val
        else:
            print("输入错误，只能输入：{}".format("、".join(choices_dict.keys())))


def get_console_select(name, message, choices):
    """
    命令行select: 显示选项列表，并允许选择其中一个选项 (方向键选择)
    Args:
        name:
        message:
        choices:

    Returns:

    """
    while True:
        questions = [
            inquirer.List(name=name, message=message + "【使用↑↓方向键选择, 回车确认】", choices=choices),
        ]
        answers = inquirer.prompt(questions)
        version = answers[name]
        if version in choices:
            return version
        else:
            print("您输入的{}不支持！！！, 输入值:{}, 允许值:{}".format(name, version, ",".join(choices)))


def get_console_select_by_map(name, message, choices_map):
    """
    命令行select: 显示选项列表，并允许选择其中一个选项, 选项展示为: map的key - map的value ; 选中后, 值为map的key
    Args:
        name:
        message:
        choices_map: map的键和值, 都需要为基础数据类型

    Returns:

    """
    choices_format_map = {}
    for k, v in choices_map.items():
        choices_format_map["{} - {}".format(k, v)] = k

    return choices_format_map[get_console_select(name, message, choices_format_map.keys())]
