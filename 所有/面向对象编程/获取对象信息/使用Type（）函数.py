# 判断对象类型，使用type（）函数
# 基本类型
print(type(123))
print(type('str'))
print(type(None))

# 变量指向函数或类
print(type(abs))

print(type(123) == type(456))
print(type(123) == int)

# 获得一个对象的所有属性和方法，使用dir（）函数，它返回一个包含字符串的list
# 获得一个str对象的所有属性和方法

# 使用dir（）获取一个对象的所有属性和方法
print(len('ABC'))
print('ABC'.__len__())


class Myobject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = Myobject()

print(hasattr(obj, 'x'))  # 有属性‘x'

print(obj.x)

print(hasattr(obj, 'y'))  # 没有属性y，返回False

setattr(obj, 'y', 19)  # 设置一个属性y

print(hasattr(obj, 'y'))  # 有属性y，返回True

print(getattr(obj, 'y'))  # 获取属性y  ，值为19

print(obj.y)  # 获取属性y

# print(getattr(obj, 'z'))    #获取没有的属性报错


print(getattr(obj, 'z', 404))  # 获取属性’z'，如果不存在，返回默认值404


#也可以获取对象的方法

print(hasattr(obj, 'power'))    #有属性‘power’，返回True

