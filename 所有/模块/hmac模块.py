# HMAC算法是一种单项加密算法，只是可以在运算过程中使用一个密钥来增强安全性
# hmac模块实现了HMAC算法，提供了相应的函数和方法

import hmac

h = hmac.new('h'.encode(), '你好'.encode())

result = h.hexdigest()
print(result)

# 原版
# h = hmac.new('h'.encode(), '你好'.encode())
# result = h.hexdigest()
# print(result)  # 获取加密后的结果
