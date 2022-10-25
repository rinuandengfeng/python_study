# sys 系统相关的功能

import sys

import random

print('hello word')

# sys.exit()     #程序退出，并且可以给一个退出码，和内置函数exit功能一致


print('呵呵呵')

# #['F:\\jichu_huanjing\\所有\\模块',
#  'F:\\jichu_huanjing',
#  'D:\\PyCharm 2020.1\\plugins\\python\\helpers\\pycharm_display',
#  'd:\\软件\\python\\python39.zip',
#  'd:\\软件\\python\\DLLs', 'd:\\软件\\python\\lib', 'd:\\软件\\python',
#  'F:\\jichu_huanjing\\venv', 'F:\\jichu_huanjing\\venv\\lib\\site-packages',
#  'D:\\PyCharm 2020.1\\plugins\\python\\helpers\\pycharm_matplotlib_backend']

print(sys.path)  # 结果是一个列表，表示查找模块的路径

sys.stdin  # 可以想input一样，用来接收用户的输入，和iput相关


sys.stdout     #标准输出，修改sys.stdout   可以改变默认输出位置


sys.stderr     #修改sys.stderr   可以改变错误输出的默认位置