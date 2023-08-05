# -*- coding: utf-8 -*-

__author__ = "mawentao119@gmail.com"

"""
Basic Operation of OS
"""

import os, stat, codecs, time, random
import shutil


def mk_dirs(path, mode=0o777):
    try:
        os.makedirs(path, mode=mode)
    except OSError:
        if not os.path.isdir(path):
            raise
def copy_file(s,d):
    try:
        shutil.copy(s,d)
    except Exception:
        return False
    return True

def copy_tree(sdir,ddir):
    try:
        shutil.copy(sdir,ddir)
    except Exception:
        return False
    return True

def walk_dir(path):
    try:
        return os.walk(path)
    except OSError:
        if not os.path.exists(path):
            raise


def list_dir(path):
    try:
        return os.listdir(path)
    except OSError:
        if not os.path.exists(path):
            raise


def exists_path(path):
    if not os.path.exists(path):
        return False

    return True


def rename_file(src, dst):
    if exists_path(src) and not exists_path(dst):
        os.rename(src, dst)

        return True

    return False


def remove_readonly(func, path, _):
    """Clear the readonly bit and reattempt the removal"""
    os.chmod(path, stat.S_IWRITE)
    func(path)


def remove_dir(path):
    shutil.rmtree(path, onerror=remove_readonly)


def remove_file(path):
    os.remove(path)


def get_splitext(path):
    return os.path.splitext(path)


def make_nod(path, mode="w", encoding="utf-8"):
    if exists_path(path):
        return False

    f = codecs.open(path, mode, encoding)

    f.close()

    return True


def write_file(path, data, mode="w", encoding="utf-8"):
    if not exists_path(path):
        return False

    f = codecs.open(path, mode, encoding)

    f.write(data)

    f.close()

    return True


def read_file(path, mode="r", encoding="utf-8"):
    if not exists_path(path):
        return {"status": False, "data": ""}

    f = codecs.open(path, mode, encoding)

    data = f.read()

    f.close()

    return {"status": True, "data": data}


def gen_outputdir():
    """生成统一的输出目录，此函数在webui内有重复"""
    t = time.strftime("%Y%m%d%H%M%S", time.localtime())
    r = random.randint(100, 999)
    dir_name = "{}_{}".format(t, r)
    out_dir = os.path.join(os.environ["PROJECT_DIR"], 'output', dir_name)
    return out_dir


def get_projectnamefromkey(key):
    # "//a/b/c/workspace/user/project/dir1/dir2/abc.robot --> project"
    # return key.split("workspace")[1].split('/')[2]
    return os.environ["PROJECT_NAME"]


def get_ownerfromkey(key):
    return 'Admin'



