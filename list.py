###list:-
#List is a collection of ordered elements
###List is a mutable data structure(make some changes)
###list is represented as []
###Syntax:- LIST_NAME=[OBJ1,OBJ2,OBJ3,....OBJN]

'''
OPERATIONS:
'''
'''
#mobiles=['iphone','samsung','vivo']
#mobiles.insert(2,'redmi')
#print(mobiles)
'''
'''
#mobiles=['iphone','samsung','vivo']
#print(mobiles[1])  or [2],[3]
'''
'''
#mobiles=['iphone','samsung','vivo']
#mobiles.append('oppo')
#print(mobiles)
'''
'''
#mobiles=['iphone','samsung','vivo']
#mobiles.pop(0)
#print(mobiles)
'''
'''

#mobiles=['iphone','samsung','vivo']
#mobiles.remove('samsung')
#print(mobiles)
'''
'''
#mobiles=['iphone','samsung','vivo']
#mobiles[1]='blackberry'
#print(mobiles)
'''
'''
###printing the elements if list
#mobiles=['iphone','samsung','vivo','redmi','nothing']
#count=1
#for ele in mobiles:
    #print(count,ele)
    #count+=1
'''
'''
###printing even numbers
mobiles=['iphone','samsung','vivo','redmi','nothing']
for i in range(0,len(mobiles)):
   if i%2==0:
        print(mobiles[i])
        '''

'''
###reversing the list 
mobiles=['iphone','samsung','vivo','redmi','nothing']
for i in range(0,len(mobiles)):
    if i%2==0:
        rev=mobiles[i]
        print(rev[::-1])
    else:
        print(mobiles[i])
'''
'''
mobiles=['iphone','samsung','vivo','redmi','nothing']
del mobiles
print(mobiles)
'''
'''
arr=[1,2,3,4,5]
k=2
first=arr[k-1:]
first=first[::-1]
second=arr[:k-1]
print(first+second)

'''






















    
