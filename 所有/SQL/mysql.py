import pymysql

#打开数据库连接
db = pymysql.connect(user='root', passwd='root',database='test')

#使用 cursor（） 方法创建一个游标对象
cursor = db.cursor()

#使用cursor（）方法执行SQL查询
cursor.execute("select version()")

#使用cursor（）方法获取单挑数据
data = cursor.fetchone()

print("Database version:%s" % data)

#关闭数据库连接
db.close()

