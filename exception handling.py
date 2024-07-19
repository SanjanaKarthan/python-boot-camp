'''
1)EXCEPTION:
            can be handled

2)BUG:
       any feature that is not working properly
3)ERROR:
      the mistake while writing the code

the error which occur
'''

#####KEYWORD IN PYTHON###

'''try,except,else,finally'''

###example:-
'''
try:
    a=10
    b=0
    c=a/b
    print(c)
except Exception:
    print('Divide by zero is not possible')
'''

'''
try:
    a=10
    b=0
    c=a/b
    print(c)
except Exception:
    print('Divide by zero is not possible')
    n1=100
    n2=200
    print(n1+n2)
    a1=1000
    a2=2000
'''
'''
try:
    a=5
    print(b)
except NameError:
    print('variable b is not assigned')
'''
'''
try:
    arr=[1,7,8,12,36]
    print(arr[8])  ###4
except IndexError:
    print('cannot access index value')
'''
'''
try:
    arr=[1,7,8,12,36]
    print(arr[4])  
except IndexError:
    print('cannot access indes value')
else:
    print('no exception occured')
'''
'''
try:
    arr=[1,7,8,12,36]
    print(arr[4])  
except IndexError:
    print('cannot access indes value')
else:
    print('no exception occured')
finally:
    print('Finally wednesday is the last day of training')
'''


    
