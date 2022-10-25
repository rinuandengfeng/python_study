import pymysql

# 连接数据库
conn = pymysql.connect(user='root', passwd='root', database='test')

# 使用cursor（）方法获取游标
cursor = conn.cursor()

# sql语句
sql = "delect from employee where age > %s " % (20)
try:
    #执行sql语句
    cursor.execute(sql)
    #提交修改
    conn.commit()
except:
    conn.rollback()

#关闭连接
conn.close()
