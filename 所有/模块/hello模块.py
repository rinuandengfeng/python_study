# ！/usr/bin/env python3
# -*- coding:utf_8 -*-
# 前两行为标准注释
# 第2行标是.py文件本身使用标准UTF—8编码


'a text module'  # 字符串，表示模块的文档注释，任何模块代码的第一个字符串
# 都被视为模块的文档注释


# 用__author__变量把作者写进去，
__author__ = 'michael liu'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print("hello,world")
    elif len(args) == 2:
        print('hello,%s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()

import  sys

if __name__ =='__main__':
    test()

