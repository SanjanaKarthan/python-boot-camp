#generate random no7.btween 1-10

'''
import random
ran=random.randint(1,10)#8
print(ran)
'''
import random
ran=random.randint(1,10)
chances=1
while chances<=3:
    guess=int(input('Enter the number'))
    ran=guess
    if guess==ran:
        print('congrats')
        break
    else:
        chances+=1
        continue
if chances>3:
    print('Failed try next time')
    
