


print('-' * 30)
print('     名片管理系统 v1.0      ')
print('1:添加名片')
print('2:删除名片')
print('3:修改名片')
print('4:查询名片')
print('5:显示所有名片')
print('6:退出系统')
print('-'*30)
x = input('请输入要进行的操作（数字）：')
while True:
    if x == 1:
        input('请输入姓名：')
        input('请输入手机号：')
        input('请输入QQ号：')
