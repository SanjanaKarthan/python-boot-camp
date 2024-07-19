'''
###RECURSION:-It calls itself

while using recursion we should not use loops
'''

###FACTORIAL WITHOUT USING RECURSION###
'''
n=5
fact=1
for i in range(1,n+1):
    fact=fact*n
print(fact)
'''

'''
###WITH USING RECURSION###

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input())
print(fact(n))

'''

###SUM OF NATURAL NUMBERS###
'''
def sum_of_natural(n):
    if n==1:
        return 1
    else:
        return n+sum_of_natural(n-1)
print(sum_of_natural(5))
'''







































