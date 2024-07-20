'''
n=int(input())
ch='*'
ch2=' '
for i in range(1,n+1):    
    print(ch*i)
'''

'''
n=int(input())
ch='*'
ch2=' '
for i in range(1,n+1):
    if i==n:
        print(ch*i)
    else:
        print(ch2*(n-i-1),ch*i)

'''

'''
n=int(input())
ch='*'
ch2=' '
for i in range(1,n+1):
    if i==n:
        print(ch*((2*i)-1))
    else:
        print(ch2*(n-i-1),ch*((2*i)-1))
'''

n=int(input())
ch='*'
ch2=' '

for i in range(1,n+1):
    if i==n:
        print(ch*((2*i)-1))
    else:
        print(ch2*(n-i-1),ch*((2*i)-1))
for i in range(n-1,0,-1):
    if i==n-1:
        print('',ch*((2*i)-1))
    else:
        print(ch2*(n-i-1),ch*((2*i)-1))
# n=3
