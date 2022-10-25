def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)


person('user',6)

person('bod',35,city='beijing')

person('adam',45 ,gender='m',job='engineer')

extra={'city':'beijing','job':'Engineer'}
person('joack',24,**extra)
