import numpy as np 

key = input("key ")
pt = input("plain text ")
keylist = []
ptlist = []
for i in key:
    keylist.append(ord(i)-97)

temp = np.array(keylist)
x = temp.reshape(3,3)


for i in pt:
    ptlist.append(ord(i)-97)

temp2 = np.array(ptlist)

msg = [[0] for i in range(3)] 
mul = []
modans = []
temp=""
i = 0
print("Cipher Text: ",end="")
for t in range(len(ptlist)//3):
    j = 0
    while j<3:
        msg[j] = ptlist[i]
        i = i +1 
        j = j +1 
    y = np.array(msg)
    
    mul  = x.dot(y) 
    modans = mul % 26
    for p in modans:
        temp = temp + chr(p+97)
        print(chr(p+97),end="")
print(end="\n")
temp3= []
for q in temp:
    temp3.append(ord(q)-97) 

xx = np.linalg.inv(x)
xxx = xx.astype(int)
print("Plain Text : ",end="")
i= 0
mul = []
for t in range(len(ptlist)//3):
    j = 0
    while j<3:
        msg[j] = temp3[i]
        i = i +1 
        j = j +1 
    y = np.array(msg)
    
    mul  = xxx.dot(y) 
    ans = mul % 26
    for p in ans:
       print(chr(p+97),end="")


    
    
    
    
