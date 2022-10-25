def foo(s):
    n = int(s)

#assert 的意思是，表达式 n!=0应该返回True
    assert n != 0,'n is zero!'
    return 10 / n

def  main():
    foo('0')
