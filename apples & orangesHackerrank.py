s=7
t=11
a=3
b=15
g=15
Apples=[6,5,-4]
Oranges=[9,8,-4]
acount,ocount=0,0
for i in Apples:
    if a+i in range(s,t+1):
        acount+=1
for i in Oranges:
    if b+i in range(s,t+1):
        ocount+=1
print(acount,ocount)
