
#Balanced brackets
#if stack is empty then it is balanced
#otherwise unbalanced
#({}[-unbalanced
#s='{[()]}'-balanced

#s='{[()]}'

    

s='{[()]}'
#if stack is empty then it is balanced
#if stack is not empty then it is unbalance
open_brackets=['(','[','{']
stack=[]
for i in s:
    if i in open_brackets:
        stack.append(i)
    else:
        if i==')' and stack[-1]=='(':
            stack.pop()
        elif i=='}' and stack[-1]=='{':
            stack.pop()
        elif i==']' and stack[-1]=='[':
            stack.pop()
        else:
            continue
if stack==[]:
    print("Balanced")
else:
    print("Unbalanced")
