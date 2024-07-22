#Example-1:
'''
Output:-
*
**
***
****
*****
'''
#--------------------------------
#code:-
'''
n=5
for i in range(1,n+1):
    print('*'*i)
'''
#----------------------------------

#Example-2:
'''
output:-
*       *
    *
*       *
'''
#Code:-
n=5
for i in range(0,n):
    for j in range(0,n):
        if i==j or i+j==n-1:
            print('*',end='')
    else:
        print(' ',end='')
print()
