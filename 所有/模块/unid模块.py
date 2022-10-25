import uuid

# unid模块

print(uuid.uuid1())  # 根据时间戳和机器码生成uuid，可以保证全球唯一
print(uuid.uuid4())  # 随机生成uuid，可能会有重复

# 使用命名空间和字符串生成uuid
# 注意以下两点：
# 1.命名空间不是随意输入的字符串，它也是一个uuid类型的数据
# 2.相同的命名空间和想到的字符串，生成的uuid是一样的


print(uuid.uuid3(uuid.NAMESPACE_DNS, 'hello'))
print(uuid.uuid5(uuid.NAMESPACE_OID, 'heelo'))
