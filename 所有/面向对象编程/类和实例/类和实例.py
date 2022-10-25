#面向对像是最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有想用的方法，但各自的数据可能不同。

#在python中，定义类（Class）是通过class关键字：
class Studen(object):
    pass
#class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是（object），表示该类是从哪个类继承下来的，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。


#可以根据定义的类Student类创建出Student的实例，创建实例是通过类名+（）实现的：
bart = Studen()  #bart变量指向的就是一个Student实例，0x00000183132180A0这个为内存地址，每个对象（objeact）的地址都不一样，而Stuent本身则是一个类
#现在bart就是一个实例

print(bart)
print(Studen)

#可以自由的给一个实例编订属性，for instance ，给实例bart半丁一个name属性：
bart.name = 'Bart Simpaon'
print(bart.name)


#类可以起到模板的作用，thus ，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：


#注：__init__方法的第一个参数永远是自己（self），表示创建的实例本身，thus，在__init__方法内部，就可以把各种属性绑定到self，因为self就是指向创建的实例本身。
#有了__init__方法，在创建实例的时候，就不能传入空的参数，必须传入__init__方法匹配人的参数，但self不需要传

class Student(object):
    #特殊方法“__init__"前后分别有两个下划线！！！
    def __init__(self,name,score):
        self.name = name
        self.score = score

bart = Student('Bart Simpson',59)
print(bart.name)
print(bart.score)

def print_score(std):
    print('%s:%s' % (std.name, std.score))


print(print_score(bart))
#在类中第一的函数只有一点不同，就是第一个参数永远是实例变量自己（self），
# also，调用时，不用传递参数，其他的类跟其他函数没有区别，所以类可以用默认参数、可变参数、关键字参数和命名关键字参数

