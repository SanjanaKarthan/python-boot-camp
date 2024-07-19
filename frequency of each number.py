####COUNT THE FREQUENCY OF EACH NUMBER#####
'''
1:2
3:2
6:1
2:1
5:2
7:1
'''

'''
arr=[1,3,6,2,5,3,7,5,1]
count=0
d={}
for key in arr:
    if key not in d:
        d[key]=1
    else:
        d[key]+=1
print(d)
'''

###TO PRINT UNIQUE ELEMENTD(which are not repeated 6,2,7)#####
'''
arr=[1,3,6,2,5,3,7,5,1]
count=0
d={}
for key in arr:
    if key not in d:
        d[key]=1
    else:
        d[key]+=1
for num,count in d.items():
    if count==1:
        print(num)
'''

###TO PRINT REPEATED VALUES(which are repeated 1,3,5)###
'''
arr=[1,3,6,2,5,3,7,5,1]
count=0
d={}
for key in arr:
    if key not in d:
        d[key]=1
    else:
        d[key]+=1
for num,count in d.items():
    if count>1:
        print(num)
'''

###keys are ages of voters and values are votes###

bjp={
    7:5,
    18:22,
    32:8,
    71:5,
    66:6
    }     
cong={
    7:15,
    18:20,
    32:4,
    71:9,
    66:2
    }
bjp_sum=0
cong_sum=0
for age,votes in bjp.items():
    if age>=18:
        bjp_sum+=votes
for age,votes in cong.items():
    if age>=18:
        cong_sum+=votes
diff=abs(bjp_sum-cong_sum)      ###abs means:absolute
if bjp_sum>cong_sum:
    print('bjp win: ',diff)
else:
    print('cong win: ',diff)




