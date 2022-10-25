# 只允许对Student实例添加name和age属性，在定义class的时候
# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性

class Student(object):
    # 用tuple定义允许绑定的属性名称
    __slots__ = ('name', 'age')


s = Student()
s.name = 'Michael'
s.age = 25
#绑定元组外的属性，会报错
# s.score = 99

#__slots__定义的属性仅对当前类实例起作用，对继承的子类不起作用
#子类定义__slots__,即可限制
class GraduateStudent(Student):
    pass
g = GraduateStudent()

#不报错，可以绑定
g.score = 99
