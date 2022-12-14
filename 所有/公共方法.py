# + :可以用来拼接，用于 字符串、元组、列表
print('hello' + 'world')
print([1, 2, 3] + [4, 5, 6])


# - :只能用于集合，求差集
print({1,2,3} - {3})

# *:可以用于字符串、元组、列表，表示重复多次。不能用于字典和集合
print('hello'*3)
print([1,2,3]*3)
print((1,2,3)*3)


# in:成员运算符
print('a' in 'abcc')
print( 1 in [1,2,3])
print(4 in (6,4,5))


#in用于字典是用来判断key是否存在
print('zhangsan' in {'name': 'zhangsan', 'age': '18', 'height': '180cm'})
print('name' in {'name': 'zhangsan', 'age': 18,'height': '180cm'})
print(3 in {3, 2, 5})

#遍历：通过for....in...我们可以遍历字符串、列表、元组、集合等可迭代对象。


#nums = [19,82,39,12,34,58]
nums = (19,82,39,12,34,58)
#nums = {19,82,39,12,34,58}
#带下标的遍历  enumerate 类的使用，一般用于列表和元组等有序的数据
for i,e in enumerate(nums):
    print('第%d个数据是%d' % (i,e))

person = {'name':'zhangsan','age':18,'height':'180cm'}
for i,k in enumerate(person):
    print(i,k)
