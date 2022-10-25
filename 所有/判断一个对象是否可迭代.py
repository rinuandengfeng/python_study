from collections import Iterable
#str是否可迭代
print(isinstance('abc',Iterable))
#list是否可迭代
print(isinstance([1,2,3],Iterable))

#整数是否可迭代
print(isinstance(123,Iterable))
