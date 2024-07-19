###fibnocci series55
#n=8
#0 1 1 2 3 5 8 13
####NORMAL USER HAVE TO GIVE INPUT
'''
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))
'''
###STARTING INDEX FROM 1
'''
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=5
print(fib(n-1))
'''
###FINDING NTH FIBONACCI SERIES(starting indes from 0)
'''
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=5
print(fib(n))
'''
