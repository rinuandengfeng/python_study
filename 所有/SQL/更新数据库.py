import pymysql

# 连接数据库
conn = pymysql.connect(user='root', passwd='root', database='test')

# 使用cursor（）方法获取游标

cursor = conn.cursor()

# sql更新语句
sql = "update employee set age = age + 1 where sex = '%C' % ('M')"

try:
    #执行sql语句
    cursor.execute(sql)
    #提交数据
    conn.commit()
except:
    #发生错误时回滚
    conn.rollback()

#关闭数据库连接
conn.close()
