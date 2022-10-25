import pymysql

# 连接数据库
conn = pymysql.connect(user='root', passwd='root', database='test')

# 使用cursor（）方法创建游标
cursor = conn.cursor()

# sql查询语句

sql = """select * from  employee where income > 1000"""

try:
    # 执行sql语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print('fanem = %s , lanem = %s , age = %s , sex = %s , income = %s ' % \
              (fname, lname, age, sex, income))
except:
    print("Error:unable to fetch data")

# 关闭连接
conn.close()
