# 一个模块本质上就是一个py文件
# 自己定义一个模块，其实就是自己写一个py文件
# import 我的模块   如果一个py文件想要当做一个模块被导入，文件名必须符合命名规范
# 由数字、字母下划线组成，不能以数字开头


# 导入一个米快，就能使用这个模块里变量和函数

import my_module

# 使用from <module_name> import * 导入这个模块里“所有”的变量和函数
# 本质是读取模块里的__all__属性，看这个属性里定义了哪些变量和函数
# 如果模块里没有定义__all__ 才会导入所有不以_开头的变量和函数
from demo import *

import demo

print(demo.n)
# import false

print(my_module.a)
my_module.test()

# 使用from demo import *  写法，不再需要写模块名
print(m)
test()
# print(n)

from hello import *

# import hello
print(x)
print(y)
# print(_age)

import hello

print(hello._age)

hello._bar()
