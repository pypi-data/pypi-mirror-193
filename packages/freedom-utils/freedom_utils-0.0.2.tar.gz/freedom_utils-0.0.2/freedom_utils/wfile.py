import json
import os
import sys
import csv
import hashlib
from pathlib import Path


def read_json(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as load_f:
            src_json_result = json.load(load_f)
        return src_json_result
    except:
        return None


def write_json(json_path, json_data, indent=None):
    """
    写入json
    Args:
        json_path: json文件路径
        json_data: json内容
        indent: 缩进, 输入正整数格式化(一般为4)

    Returns:

    """
    mkdir_if_not_exist(os.path.split(json_path)[0])
    str_json_result = json.dumps(json_data, ensure_ascii=False, indent=indent)
    with open(json_path, 'w', encoding='utf-8') as f:
        f.write(str_json_result)


def mkdir_if_not_exist(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def write_file(file_mame, content):
    with open(file_mame, 'w', encoding="utf-8") as file:
        for line in content:
            line = line + '\n'
            file.write(line)


def write_csv(file_mame, content):
    if os.path.exists(file_mame):
        os.remove(file_mame)
    mkdir_if_not_exist(os.path.split(file_mame)[0])
    with open(file_mame, 'w', encoding="utf-8-sig", newline="") as f:
        csv_write = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        csv_write.writerows(content)


def find_files(root_path, suffixes):
    all_file_paths = []
    for suffix in suffixes:
        file_paths = Path(root_path).rglob(suffix)
        all_file_paths.extend(file_paths)
    return all_file_paths


def make_url_md5(http_url):
    return hashlib.md5(http_url.encode()).hexdigest()


