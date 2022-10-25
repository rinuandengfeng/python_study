class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

#调用对象对应关联的函数，称之为对象的方法
    def print_score(self):
        print('%s:%s' % (self.name, self.score))


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

bart.print_score()
lisa.print_score()