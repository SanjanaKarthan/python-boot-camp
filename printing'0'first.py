#printing '0' first after '0' printing '1'
#arr=[1,2,0,1,1,0,0]
#output:0,0,0,1,1,1,1
'''
arr=[1,1,0,1,1,0,0]
ones=[]
zeroes=[]
for i in arr:
    if i==0:
        zeroes.append(i)
    else:
        ones.append(i)
zeroes.extend(ones)
print(zeroes)
'''

#same question in different logic
'''
arr=[1,1,0,1,1,0,0]
result=[]
for i in arr:
    if i==0:
        result.insert(i,0)
    else:
        result.append(i)
print(
'''


