import pymysql

#打开数据库连接
conn = pymysql.connect(user = 'root' , passwd = 'root' , database = 'test')

#使用cursor（）方法获取游标
cursor = conn.cursor()

#SQL插入语句

sql = """insert into employee (FIRST_NAME , 
        LAST_NAME , AGE , SEX , INCOME) 
            value ('Mac' , 'Mohan' , 20 , 'M' , 2000)"""

try:
    #执行sql语句
    cursor.execute(sql)
    #提交到数据库执行
    conn.commit()
except:
    #如果发生错误则回滚
    conn.rollback()

#关闭数据库连接
conn.close()



