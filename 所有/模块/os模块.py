# os 全称  OperationSystem操作系统
# os  模块里提供的方法就是用来调用操作系统里的方法

import os

# os.name   ==> 获取操作系统的名字  Windows系列 ==>nt  /   非windows ==>posix
print(os.name)  # nt

print(os.sep)  # 路径的分隔符  windows  \     非Windows  /

# os模块里的path模块经常使用


# abspath ==>获取文件的绝对路径
print(os.path.abspath('高阶函数.py'))  # F:\jichu_huanjing\所有\模块\高阶函数.py

# isdir判断是否是文件夹
print(os.path.isdir('导入模块.py'))  # False
print(os.path.isdir('xxx'))  # True

# isfile 判断是否是文件
print(os.path.isfile('导入模块的语法.py'))  # True
print(os.path.isfile('xxx'))  # False

# exists  判断是否存在
print(os.path.exists('作用域.py'))  # True
print(os.path.exists('mmm.py'))  # False

file_name = '2020.2.21.demo.py'
# print(file_name.rpartition('.'))
print(os.path.splitext(file_name))

file_name = '2020.2.21.demo.py'
print(file_name.rpartition('.'))
print(os.path.splitext(file_name))

# os里的其他方法的介绍


# 获取当前的工作目录，即当前python脚本工作的目录
os.getcwd()

# 改变当前脚本工作目录，相当于shell下的cd命令
# print(os.chdir('test.py'))

# 文件重命名
# os.rename('毕业论文.txt','毕业论文-最终版.txt')


# 删除文件
os.remove('毕业论文.txt')

# 删除空文件夹
os.removedirs('demo')

# 创建一个文件夹
os.mkdir('demo')

# 切换工作目录
os.chdir('c:\\')

# 列出指定目录里的所有文件和文件夹
os.listdir('c:\\')
