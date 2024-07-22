#Day-3 task 1
## alice=[10,3,6]
#bob=[12,3,4]
#a,b,=0,0
#a=1
#b=1

#code:-
'''
alice=[10,3,6]
bob=[12,3,4]
a,b=0,0
for i in range(len(alice)):
    if alice[i]>bob[i]:
        a+=1
    elif alice[i]<bob[i]:
        b+=1
    else:
        continue
print('alice:',a)
print('bob:',b)
--------------------------------------------------------------
'''
'''
#day-3 Task 2  {QUESTION ASKED IN TECH MAHINDRA}
#Password validation:
-you are given a string s, check whether the string is vaild passwoed or not.
-password is "valid" if the string satisfies the below conditions else the string is
-use check function
#coditions:-
-length(password) >8
-password should contain atleast
   ->1 capital letter
   ->1 small letter
   ->1 digit
   ->1 special character
Input format:-
-take a string s as input
Sample input:-
s='Excellence@123
'''
#Code:-
'''
def check(S):
    #special_char=['!','@','#','$','%','^','&','*','`','?']
    up_c,low_c,sp_c,dig_c=0,0,0,0
    if len(S)>8:
        for i in range(len(S)):
            if S[i].isdigit():
                dig_c+=1
            elif S[i].isupper():
                up_c+=1
            elif S[i].islower():
                low_c+=1
            elif S[i].isascii():
                sp_c+=1
            else:
                break
        if dig_c>0 and up_c>0 and low_c>0 and sp_c>0:
            print("valid")
        else:
            print("invalid")
    else:
        print("invalid")
string=input()
check(string)
'''

s=input()
ucount,lcount,dcount,scount=0,0,0,0
for c in s:
    if c.isupper():
        ucount+=1
    elif c.islower():
        lcount+=1
    elif c.isdigit():
        dcount+=1
    else:
        scount+=1
if len(s)>0 and ucount>0 and lcount>0 and dcount>0 and scount>0:
    print('valid')
else:
    print('invalid')
