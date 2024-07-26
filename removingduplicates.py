
s='hello world hello world good morning good afternoon'

#Remove duplicate words
#output:
    #hello world good morning afternoon



#code:-1
'''
s=s.split()
s1=''
for i in s:
    if i not in s1:
        s1=s1+i+' '
print(s1)
'''
#Example 2:-
#with dictonary
s=s.split()
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]=1
s1=''
for k,v in d.items():
    if v>=1:
        s1+=k+' '
print(s1)

    
