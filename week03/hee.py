

'''
#test


k = [1,2,3,4,5]
star = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5'}

for i ,v in enumerate(k):
    star = star[i] if star  else 

print(star)    '''

import pymssql
#conn = pymssql.connect(r"SERVER='192.168.20.10,1433';DATABASE='Healthone';UID='sa';PWD='Admin123' ")


conn=pymssql.connect(server='192.168.20.10',user='sa',password='@jkcin#&tn%$viy123',database='Healthone',charset = 'utf8')
ccc = conn.cursor()


sql = "select top 10  * from tuser"
try:
    ccc.execute(sql)  # 执行sql语句

    results = ccc.fetchall()  # 获取查询的所有记录
    print("id", "id2", "name","name2","name3","name4" ,"name5")
    # 遍历结果
    for row in results:
        a1=row[0]
        a2=row[1].encode('latin-1').decode('gbk')
        a3=row[2].encode('latin-1').decode('gbk')
        a4=row[3].encode('latin-1').decode('gbk')
        a5=row[4].encode('latin-1').decode('gbk')
        a6=row[5].encode('latin-1').decode('gbk')
        a7=row[6].encode('latin-1').decode('gbk')
        print('{:>12}{:>12}{:>12}{:>12}{:>12}{:>20}{:>12}'.format(a1,a2,a3,a4,a5,a6,a7))


except Exception as e:
    raise e
finally:
    conn.close()  # 关闭连接
