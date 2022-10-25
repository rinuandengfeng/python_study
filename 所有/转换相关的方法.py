#内置类  list tuple set
nums = [9,8,4,3,2,1]
x = tuple(nums)  #使用tuple内置类转化成为元组
print(x)

y = set(nums)    #使用set内置类转换成为集合
print(y)


z = list({'name':'zhangsan','age':18,'score':98})
print(z)

#python里有一个比较强大的内置函数eval，可以执行字符串里的代码
a = 'input("请输入那您的用户名")'   #a是一个字符串
#eval(a)              #eval是执行字符串里面的代码
b = '1+1'
print(eval(b))


import json

#JOSN的使用，把列表、元组、字典等转换成JOSN字符串

person = {'name':'zhangsan','age':18,'gender':'female'}
#自带你如果就想要把它传给前端页面或者字典写到一个文件里
m = json.dumps(person)   #dumpus将字典、列表、集合、元组等转换成为JOSN字符串
print(m)  # '{"name":"zhangsan“,”age“:18,”gender":"female"}'  JOSN里面必须用双引号
#print(type(m))   #<class 'str'>


#print(m['name'])     不能这样使用，m是一个字符串，不能再像字典一样根据key获取value



#python                             json
#True                               True
#False                              False
#字符串                              字符串
#字典                                对象
#列表、元组                           数组

print(json.dumps(['hello','good','yes',True]))
print(json.dumps(('hello','good','yes',False)))


n = '{"name":"lisi","age":20,"gender":"male"}'
n = '["hello","good"]'
#p = eval(n)
#print(type(n))
s = json.loads(n)   #loads可以将josn字符串转换称为python里的数据
print(s)
print(type(s))






