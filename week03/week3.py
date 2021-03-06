import pymysql
from sqlalchemy import create_engine, Table, Column, String, Integer, DateTime, Enum, or_, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy import desc
from datetime import datetime

import pymssql

conn = pymssql.connect(r'SERVER=192.168.20.10,3433;DATABASE=Healthone;UID=sa;PWD=Admin123;db=database')

ccc = conn.cursor()

sql = "select top 10  * from tuser"
try:
    ccc.execute(sql)  # 执行sql语句

    results = ccc.fetchall()  # 获取查询的所有记录
    # print("id", "user_id", "name")
    # 遍历结果
    for row in results:
        print(row)
except Exception as e:
    raise e
finally:
    conn.close()  # 关闭连接


#import pymysql
 
# 打开数据库连接
#db = pymysql.connect("192.168.3.38","testuser","testpass#AB1234","testdb" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
#cursor = db.cursor()
 
# 使用 execute() 方法执行 SQL，如果表存在则删除
#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
''' 
# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )""" '''
'''
sql = "select * from blogs"
try:
    cur.execute(sql)  # 执行sql语句

    results = cur.fetchall()  # 获取查询的所有记录
    print("id", "user_id", "name")
    # 遍历结果
    for row in results:
        id = row[0]
        user_id = row[1]
        name = row[4]
        print(id, name, user_id)
except Exception as e:
    raise e
finally:
    db.close()  # 关闭连接
# 2.插入操作
db = pymysql.connect("localhost","root","mysql12345","awesome")
cur_insert = db.cursor()

# sql插入语句 表名blogs
sql_insert ="""insert into blogs(id,user_id,name) values ("test_id",'test_user_id','test_name')"""

try:
    cur_insert.execute(sql_insert)
    # 提交
    db.commit()
    print('开始数据库插入操作')
except Exception as e:
    db.rollback()
    print('数据库插入操作错误回滚')
finally:
    db.close()
# 打开数据库连接
db = pymysql.connect("localhost","testuser","test123","TESTDB" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()
 
# 关闭数据库连接
db.close()

# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000),('Mac1', 'Mohan', 20, 'M', 2000),('Mac2', 'Mohan2', 20, 'M', 2000),('Mac33', 'Mohan3', 20, 'M', 2000)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
   print("CREATE TABLE OK")
except:
   # 如果发生错误则回滚
   db.rollback()
 
# 关闭数据库连接
db.close() 
 # test for insert ,pass 
#cursor.execute(sql)

#print("CREATE TABLE OK")
# 关闭数据库连接
#db.close()

'''

"""
使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:
    用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
    将 ORM、插入、查询语句作为作业内容提交
"""

Base = declarative_base()

class Tuser_table(Base):
    __tablename__  = 'Tuser'
    uid = Column(Integer(), primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    age = Column(Integer())
    birthday = Column(DateTime(), default=datetime.now)
    sex = Column(Enum('男', '女'))
    education= Column(String(10), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

#dburl="mysql+pymysql://testuser:testpass@127.0.0.1:3306/testdb?charset=utf8mb4"
dburl="mysql+pymysql://testuser:testpass#AB1234@192.168.3.38:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding="utf-8")

# the first time open this line to create the table
#Base.metadata.create_all(engine)

SessionClass = sessionmaker(bind=engine)
session = SessionClass()

'''
# 
#添加数据 , 添加一次数据后，注释
add1 = Tuser_table(username='tom1', age=33, birthday='1987-1-1', sex='男', education='本科')
add2 = Tuser_table(username='tom2', age=39, birthday='1981-2-7', sex='男', education='专科')
add3 = Tuser_table(username='jack1', age=30, birthday='1990-3-4', sex='男', education='专科')
add4 = Tuser_table(username='jack2', age=39, birthday='1981-12-1', sex='男', education='本科')
add5 = Tuser_table(username='yuyu', age=30, birthday='1992-11-3', sex='男', education='本科')
add6 = Tuser_table(username='peter', age=29, birthday='1991-4-3', sex='女', education='本科')
add7 = Tuser_table(username='luxi', age=28, birthday='1992-11-3', sex='女', education='本科')
add8 = Tuser_table(username='kiki', age=28, birthday='1992-11-3', sex='女', education='本科')
session.add(add1)
session.add(add2)
session.add(add3)
session.add(add4)
session.add(add5)
session.add(add6)
session.add(add7)
session.add(add8)
session.commit()

'''


#查询数据
result = session.query(Tuser_table.username, Tuser_table.age,  func.date_format(Tuser_table.birthday, "%Y-%m-%d"), Tuser_table.sex, Tuser_table.education).all()
for i in result:
    print(i)

#排序查询根据年龄
print("排序查询")
result = session.query(Tuser_table.username, Tuser_table.age,  func.date_format(Tuser_table.birthday, "%Y-%m-%d"), Tuser_table.sex, Tuser_table.education).order_by(desc(Tuser_table.age))
for i in result:
    print(i)

#条件查询根据学历和性别
#yy = session.query(Tuser_table.username, Tuser_table.age,  func.date_format(Tuser_table.birthday, "%Y-%m-%d"), 
                     #  Tuser_table.sex, Tuser_table.education).filter(and_(Tuser_table.education == "本科", Tuser_table.sex == "男")).all()

print("条件查询")
result = session.query(Tuser_table.username, Tuser_table.age,  func.date_format(Tuser_table.birthday, "%Y-%m-%d"), 
                       Tuser_table.sex, Tuser_table.education).filter(and_(Tuser_table.education == "本科", Tuser_table.sex == "男")).all()
for i in result:
    print(i)
session.commit() 