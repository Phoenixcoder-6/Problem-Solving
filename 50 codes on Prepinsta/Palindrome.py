def palindrome(str):
    str1= str[::-1]
    if str==str1:
        print("Palindrome")
    else:
        print("Not Palindrome")


str="madam"
palindrome(str)