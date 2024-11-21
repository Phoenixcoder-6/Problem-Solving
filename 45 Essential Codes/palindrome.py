def palindrome_check(string):
    rev= string[::-1]

    if string==rev:
        return "Palindrome"
    else:
        return "Not Palindrome"
    
string="abcba"
res= palindrome_check(string)
print(res)
