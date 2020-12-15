import pymysql
from sqlalchemy import create_engine, Table, Column, String, Integer, DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()
# 用户表
class Users_table(Base):
    __tablename__  = 'users'
    uid = Column(Integer(), primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
# 用户资产表
class Assets_table(Base):
    __tablename__  = 'userassets'
    id = Column(Integer(), primary_key=True)
    zid = Column(Integer(), ForeignKey(Users_table.uid))
    username = Column(String(20), nullable=False, unique=True)
    assetsnum = Column(Integer(), default=0)
# 审计用表
class Audit_table(Base):
    __tablename__  = 'audit'
    #id = Column(Integer(), primary_key=True)
    id = Column(Integer, primary_key=True, autoincrement=True)
    transfer_time = Column(DateTime(), default=datetime.now)
    # 被转用户
    username_in = Column(String(20), nullable=False, unique=False)
    # 被转用户id
    inid = Column(Integer(), ForeignKey(Users_table.uid))
    # 转账用户
    username_out = Column(String(20), nullable=False, unique=False)
    # 转账用户id
    outid = Column(Integer(), ForeignKey(Users_table.uid))
    transfer_amount = Column(Integer())

class Thing:
    @classmethod
    def go(cls,session,a):
        #获取转账用户名
        namea= session.query(Users_table.username).filter(Users_table.uid == a).first()
        return namea[0]

class Thing2:
    @classmethod
    def go(cls,session,b):
        #获取收款用户名
        nameb= session.query(Users_table.username).filter(Users_table.uid == b).first()
        return nameb[0]
    
class Thing3:
    @classmethod
    def go(cls,session,a,qian):
        #扣款
        kou = session.query(Assets_table.username, Assets_table.zid, Assets_table.assetsnum).filter(Assets_table.zid == a)
        print(kou.first()[2],"==",type(kou.first()[2]))
        having = kou.first()[2]
        if having <qian:
            print(57)
            raise
        else:
            kou.update({Assets_table.assetsnum: having-qian})
            print("扣钱了")

class Thing4:
    @classmethod
    def go(cls,session,b,qian):
        # 收款
        jia = session.query(Assets_table.username, Assets_table.zid, Assets_table.assetsnum).filter(Assets_table.zid == b)
        print(122)
        having = jia.first()[2]
        jia.update({Assets_table.assetsnum: having + qian})
        print("进账了")

class Thing5:                                 # 还有问题，需要改，如何写插入，有问题，需要帮助
    @classmethod
    def go(cls,session,a,b,aa,bb,m):
        #记录到转账审计表
        print(77)
        auditadd=Audit_table(username_out=aa, username_in=bb, outid=a, inid=b, transfer_amount=m)
        #h = Audit_table(username_out= aa, username_in= bb, outid= a, inid= b, transfer_amount= m)
        print(79)
        session.add(auditadd)
        print(81)
        session.flush()
        print(83)
        #res = session.query(Audit_table.outid, Audit_table.username_out, Audit_table.inid,\
                   # Audit_table.username_in, Audit_table.transfer_amount, Audit_table.transfer_amount).all()
        #print(129)
        #session.query(Audit_table.outid, Audit_table.username_out, Audit_table.inid, Audit_table.username_in, Audit_table.transfer_amount)
        print(" -----132------转账审计审计表 数据表(audit)")
        #add8 = Tuser_table(username='kiki', age=28, birthday='1992-11-3', sex='女', education='本科')
        #session.add(add8)

# 用户操作类
class User_actions():

    # 添加用户
    def user_add(self, usadd):
        SessionClass = sessionmaker(bind=self.engine)
        session = SessionClass()
        session.add(usadd)
        session.commit()

    # 添加用户资产
    def assets_add(self, asadd):
        SessionClass = sessionmaker(bind=self.engine)
        session = SessionClass()
        session.add(asadd)
        session.commit()

def run_my_program(db,a,b,m):
    engine = create_engine(db, echo=True, encoding="utf-8")
    SessionClass = sessionmaker(bind=engine)
    session = SessionClass()
    try:
        aa= Thing().go(session,a)
        bb= Thing2().go(session,b)
        #a 扣款
        Thing3().go(session,a,m)
        #b 收款
        Thing4().go(session,b,m)
        # 记录审计
        Thing5().go(session,a,b,aa,bb,m)     #--还有问题，需要改
        print(121)

        session.commit()

        print(124)
    except:
        session.rollback()
        #raise
        print("I am sorry!")
    finally:
        session.close()

if __name__ == '__main__':
    db="mysql+pymysql://testuser:testpass#AB1234@192.168.3.38:3306/testdb?charset=utf8mb4"
    a = 100
    b = 102
    money =200
    if money > 0:
        run_my_program(db,a,b,money)