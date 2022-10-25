# 给实例绑定属性的方法是通过实例变量，或者通过self变量


# class Student(object):
#     def __init__(self,name):
#         self.name = name
#
# s = Student('name')
# s.score = 90


class Student(object):
    name = 'Student'

#创建实例
s = Student()

#打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(s.name)

#打印类的name属性
print(Student.name)

#给实例绑定name属性
s.name = 'Michael'

#由于实例属性的优先级比类属性高，所以，它会屏蔽掉类的name属性
print(s.name)

#但是类的name属性并没有消失，用Student.name仍然可以访问
print(Student.name)

#删除实例的name属性
del  s.name

#再次调用，由于实例的name属性没有找到，类的name属性就显示出来了
print(s.name)

#在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，相同的名称的实例属性将屏蔽掉类属性



