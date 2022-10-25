#忽略大小写排序
print(sorted(['bob','about','Zoo','Credit'],key=str.lower))

#进行反想排序，不必改动key函数，可以直接传入第三个参数 reverse=True
print(sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True))