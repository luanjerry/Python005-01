#!/usr/bin/env python
import socket
import os
import sys


HOST = '127.0.0.1'
PORT = 10037


'''
import re
line = "week02.txt#####$#$"
 
matchObj = re.match( r'(.*) #####$#$ (.*?).*', line, re.M|re.I)
 
if matchObj:
   print( "matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")


#!/usr/bin/python
import re
 
line = "Cats are smarter than dogs"
line = "week02.txt areare"
 
matchObj = re.match( r'(.*)areare(.*)', line, re.M|re.I)
 
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!") '''


def file_client():
    ''' file Server 的 client 端 '''

    file_in = input('input your file> ')
    # win系统需要把\\字符进行处理替换
    file_in = file_in.replace("\\", "/")
    #print(file_in)
    # 判断上传文件是否存在
    if not os.path.isfile(file_in):
        print("该文件不存在")
        sys.exit()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    # 获取到文件名
    file_in_dirname = os.path.basename(file_in)
    # filename + 文件名 发送给服务端进行正则匹配处理
    file_in_name = file_in_dirname.strip()
    print(len(file_in_name))
    size=len(file_in_name)
    if size<100:
        file_in_name +='areare'
        file_in_name +="#" *(100-size-6)
    print(len(file_in_name),2)

    # 发送文件名
    s.sendall(file_in_name.encode())
    # 传输文件
    with open(file_in, "rb") as f:
            datas = f.read()
            s.sendall(datas)
    f.close()
    s.close()


if __name__ == '__main__':
    file_client()  