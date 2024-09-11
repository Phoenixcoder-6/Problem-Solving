def is_balanced(s):
    c=0
    ans=False
    for i in s:
        if i=="(" :
            c+=1
        elif i == ")":
            c-=1
        if c<0:
            return ans
        if c==0:
            return True
    return ans

s="{()}"
print(is_balanced(s))

            
