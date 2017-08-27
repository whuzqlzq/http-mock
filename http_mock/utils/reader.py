# -*- coding: UTF-8 -*-
from importlib import import_module
import glob


# 相对路径
# 搜索包下除__init__外的py文件
def get_files(rel_path='../config/*[a-z0-9].py'):
    f = glob.iglob(rel_path)

    lp = []

    for p in f:
        ps = p.split('/')
        ps = ps[-1].split('.')
        ps = ps[0]
        lp.append(ps)

    return lp


def get_params(fl=[], name='urls'):
    urls = []
    for f in fl:
        m = import_module('http_mock.config.' + f)
        for u in getattr(m, name):
            urls.append(u)

    return urls


if __name__ == '__main__':
    print get_params(get_files(), 'urls')
