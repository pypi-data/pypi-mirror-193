import os
import shutil
import chardet

from datetime import datetime
from glob import glob
from hashlib import sha1


def check_file_exist(file_path: str):
    return os.path.exists(file_path)


def check_is_file(file_path: str):
    return os.path.isfile(file_path)


def get_file_size(file_path: str):
    return os.path.getsize(file_path)


def get_file_name(file_path: str):
    return os.path.basename(file_path)


def get_file_folder(file_path: str):
    return os.path.dirname(file_path)


def get_file_create_time(file_path: str):
    return datetime.fromtimestamp(os.path.getctime(file_path))


def get_file_modify_time(file_path: str):
    return datetime.fromtimestamp(os.path.getmtime(file_path))


def get_file_access_time(file_path: str):
    return datetime.fromtimestamp(os.path.getatime(file_path))


def del_file(file_path: str):
    return os.remove(file_path)


def del_folder(file_folder: str):
    shutil.rmtree(file_folder)


def copy_file(src_file_path: str, dst_file_path: str):
    if check_file_exist(src_file_path) is True:
        dst_folder = get_file_folder(dst_file_path)
        if not os.path.exists(dst_folder):
            os.mkdir(dst_folder)
        return shutil.copyfile(src_file_path, dst_file_path)


def copy_folder(src_folder_path: str, dst_folder_path: str):
    if check_file_exist(src_folder_path) is True:
        dst_folder = get_file_folder(dst_folder_path)
        if not os.path.exists(dst_folder):
            os.mkdir(dst_folder)
        return shutil.copytree(src_folder_path, dst_folder_path)


def move_file(src_file_path: str, dst_file_path: str):
    if check_file_exist(src_file_path) is True:
        dst_folder = get_file_folder(dst_file_path)
        if not os.path.exists(dst_folder):
            os.mkdir(dst_folder)
        return shutil.move(src_file_path, dst_file_path)


def scan_files(glob_path: str, recursive: bool = False):
    return sorted(glob(glob_path, recursive=recursive))


def file_hash(file_path: str):
    if os.path.isfile(file_path):
        hash_sha1 = sha1()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha1.update(chunk)
        return hash_sha1.hexdigest()


# 比较文件
def compare_file(src_path: str, dst_path: str):
    return file_hash(src_path) == file_hash(dst_path)


# 重命名文件
def rename_file(old_path: str, new_path: str):
    if check_file_exist(old_path) is True:
        if check_file_exist(new_path) is True:
            del_file(new_path)
        os.rename(old_path, new_path)


def get_file_encoding(file_path: str):
    with open(file_path, 'rb') as f:
        return chardet.detect(f.read(1024))['encoding']
