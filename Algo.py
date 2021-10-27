#add some comments man!!
import numpy as np
import random
a=[]#store ascii map here
for i in range(0,128):
    a.append(chr(i))
#print(a)
gen=[]
for i in range(128,2048):
    gen.append(i)


key=[]
cnt=0
'''for i in range(0,128):
    b=[]
    for j in range(0,8):
        while(1):
            #c=random.randrange(0,1920)
            c=random.randrange(128,2048)
            d=0
            for k in range(0,len(key)):
                for l in range(0,8):
                    if(c==key[k][l]):
                        d=d+1
            if(d==0):
                b.append(c)
                break
    key.append(b)
print(key)
key1=set(key)
print(len(key))
print(len(key1))'''
key=random.sample(range(128, 2048), 1024)



res = []
ny=np.array(key)
ny=np.reshape(ny,1024)
cnt=0
for i in range(0,len(ny)):
    for j in range(0,len(ny)):
        if(ny[i]==ny[j]):
            if(i==j):
                continue
            else:
                cnt=cnt+1
                print("i",i)
                print("j",j)
                print(ny[i])
                print(ny[j])
print(cnt)
dup=key
key=[]
k=0
for i in range(0,128):
    b=[]
    for j in range(0,8):
        b.append(dup[k])
        k=k+1
    key.append(b)


m=input("Please enteer your message")
ct=[]
for i in range(0,len(m)):
    c=ord(m[i])
    d=random.randrange(0,8)
    ct.append(key[c][d])
    #e=random.randrange(128,2048)
    ch=0
    while(1):
        e=random.randrange(128,2048)
        ch=0
        for k in range(0,len(key)):
            for l in range(0,len(key[k])):
                if(key[k][l]==e):
                    ch=ch+1
        if(ch==0):
            ct.append(e)
            break

print(ct)
om=[]
print(key[0][0])
for i in range(0,len(ct)):
    for j in range(0,len(key)):
        for k in range(0,len(key[j]) ):
            if(ct[i]==key[j][k]):
                       om.append(chr(j))
print(om)
            







    
