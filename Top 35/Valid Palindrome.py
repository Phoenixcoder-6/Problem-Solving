def palindrome(s):
    s= s.lower()
    s1=''
    for c in s:
        if c.isalnum():
            s1+=c

    if s1== s1[::-1]:
        return True
    else:
        return False
    

s=" MissiM"
res= palindrome(s)
print(res)