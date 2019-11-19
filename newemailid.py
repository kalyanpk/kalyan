import re
num=int(input("enter the  number:"))
emailid=[]
for x in range(num):
    e=input("enter the emailid's:")
    emailid.append(e)
for i in emailid:
    mo=re.match(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',i)
    if mo:
       print("email found:",i)
