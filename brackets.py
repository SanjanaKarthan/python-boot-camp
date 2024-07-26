def check(s):
    stack=[]
    openings=['(','[','{']
    brackets={'(':')','[':']','{':'}'}
    for i in s:
        if i in openings:
            stack.append(i)
        else:
            if stack:
                top=stack.pop()
                if brackets[top]!=i:
                    return 'NO'
            else:
                return 'NO'
    if stack:
        return 'No'
    else:
        return 'Yes'
s='}{}'
print(check(s))
