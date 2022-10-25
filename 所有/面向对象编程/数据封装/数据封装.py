class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 封装数据的函数和Student类本身关联起来的，称之为类的方法。
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    # 封装的好处是可以给Student类增加新的方法
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'



bart = Student('Bart Simpson', 59)

Student.print_score(bart)

# 调用一个方法，只需要在实例变量上直接调用，self不用传递，正常传入其他变量
bart.print_score()

print(bart.get_grade())