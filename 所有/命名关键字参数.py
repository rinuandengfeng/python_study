def perxson(name,age,**kw):
    if 'city' in kw:
        #有city参数
        pass
    if'job' in kw:
        #有job参数
        pass
    print('name:',name,'age:',age,'other:',kw)

print(perxson('jack',24,city='beijing',addr='chaoyang',zipcode=123456))