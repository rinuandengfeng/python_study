import pymysql

#连接数据库
db = pymysql.connect(user="root", passwd="root", database='test')

#使用cursor（）方法创建一个游标对象cursor
cursor = db.cursor()

#使用execute() 方法执行SQL语句，如果存在则删除
cursor.execute('drop table if exists employee')

#使用预处理语句创建表

sql = """create table employee(
        first_name char(20) not null,
        last_name char(20),
        age int,
        sex char(1),
        income float)"""

cursor.execute(sql)

#关闭数据库连接
db.close()