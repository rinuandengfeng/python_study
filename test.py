# def hi(name="yasoob"):
#     def greet():
#         return "now you are in the greet() function"
#
#     def welcome():
#         return "now you are in the welcome() function"
#
#     if name == "yasoob":
#         return greet
#     else:
#         return welcome
#
# a = hi()
# print(a)
# print(a())



def hi():
    return "yasoob"

def doSomethingBeforeHi(func):
    print("I am doing some boring work before exwcuting hi()")
    print("func()")

doSomethingBeforeHi(hi)