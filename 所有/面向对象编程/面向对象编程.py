# 采用面向对象的程序设计思想，打印一个成绩表
# Sutdent这种数据类型因该被视为一个对象，这个对象有name和score这两个属性
# 要打印学生成绩表，首先必须创建出这个学生对应的对象，然后，给对象发一个print_score消息，让对象自己把自己打印出来

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s' % (self.name, self.score))


# 给对象发消息实际上就是调用对象对用的关联函数，我们称之为对象的方法。面向对象的程序写出来就是这样：

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()


#面向对象的抽象程度又比函数高，因为一个类（Class）既包含数据，又包含操作数据的方法。

#数据封装、继承和多态是面向对象的三大特点。
