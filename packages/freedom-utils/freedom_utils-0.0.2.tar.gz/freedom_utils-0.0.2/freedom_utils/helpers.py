def list_safe_remove(r_list, val):
    """
    安全的 remove 列表中元素
    Args:
        r_list:
        val:

    Returns:

    """
    (val in r_list) and r_list.remove(val)


def dict_safe_pop(r_dict, key):
    """
    安全的 pop 字典中对应key的元素
    Args:
        r_dict:
        key:

    Returns:

    """
    (key in r_dict) and r_dict.pop(key)

