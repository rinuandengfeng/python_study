import os

print(os.name)

print(os.sep)    #路径分隔符

print(os.path.abspath('os.py'))

print(os.path.isdir('os.py'))   #判断是否为文件夹

print(os.path.isdir('xxx'))

print(os.path.isfile('os.py'))

print(os.path.isfile('xxx'))

print(os.path.exists('sys模块.py'))   #是否存在


print(os.path.dirname(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

