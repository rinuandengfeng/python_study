# 定义一个calss的时候，从莫格现有的class继承，新的class称为子类
# 而被继承的class称为基类、父类或超类

class Animal(object):
    def run(self):
        print('Animal is running...')


# 当我们编写Dog和Cat类时，就可以直接Animal类继承：
class Dog(Animal):  # 对Dog来说，Animal就是它的父类 ,Dog是它的子类

    # 当子类和父类都存在相同的run（）方法时，子类的run（）覆盖父类的run（）
    def run(self):
        print('Dog is running...')

    def ect(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


dog = Dog()
print(dog.run())
print(dog.ect())

cat = Cat()
print(cat.run())

# 我们定义一个calss的时候，我们实际上就定义了一种数据类型。
# 我们定义的数据类型和python自带的数据类型例str、list、dict没什么两样

a = list()  # a是list类型
b = Animal()  # b是Animal类型
c = Dog()  # c是Dog类型
# 用isinstance()判断一个变量是否是某个类型
print(isinstance(a, list))  # True
print(isinstance(b, Animal))  # True
print(isinstance(c, Dog))  # True
# 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类，但是反过来不行
print(isinstance(c, Animal))  # True
