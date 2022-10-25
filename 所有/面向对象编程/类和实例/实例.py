# 实例是根据类创建出来的一个个具体的“对象”。
# 每个对象都拥有相同方法，但各自的数据可能不同。
class Student(object):

    # 类起到模板的作用
    # 在创建实例的时侯，可以把必须绑定的属性强制填写进去 ，通过定义特殊的__init__方法
    # __init__方法的第一个参数永远是self，表示创建实例本身
    # 可以把各种属性绑定到self，因为self指创建是实例本身
    def __init__(self, name, score):
        self.name = name
        self.score = score


# 在__init__方法，创建实例是不能传入空参数，必须传入与__init__方法匹配的参数，self不需要传
bart = Student('Bart Simpson', 59)
print(bart.name)
print(bart.score)
# 创建实例是通过类名+（）实现

# bart = Student()  # bart指向的就是一个Student的实例

print(bart)

print(Student)

# 实例变量绑定属性

bart.name = 'Bart Simson'  # 给实例bart绑定一个name属性
print(bart.name)
