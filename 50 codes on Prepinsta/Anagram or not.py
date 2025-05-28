def anagram(str1,str2):
    if (sorted(str1.lower())) == (sorted(str2.lower())): 
        print("Anagram")
    else:
        print("Not Anagram")

str1="Listen"
str2="Silent"
anagram(str1,str2)
