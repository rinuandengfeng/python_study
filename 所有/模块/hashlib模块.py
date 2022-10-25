# hashlib是一个提供字符加密功能的模块，包含MD5和SHA的加密算法，该模块在用户登录认证方面应用广泛，对文本加密也很常见。


import hashlib

# 待加密信息

str = '这是一个测试'

# 创建md5对象
h1 = hashlib.md5('hello'.encode(encoding='utf8'))

print('MD5加密后为：' + h1.hexdigest())

h1 = hashlib.sha1('123456'.encode())
print('sha加密后为：', h1.hexdigest())
h2 = hashlib.sha3_224('123456'.encode())
print('sha3_224加密后为：', h2.hexdigest())

h3 = hashlib.sha3_256('123456'.encode())
print('sha3_256加密后为：', h3.hexdigest())
h4 = hashlib.sha3_384('123456'.encode())
print('sha3_384加密后为：', h4.hexdigest())
