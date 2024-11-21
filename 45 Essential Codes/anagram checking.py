def anagram_checking(string1,string2):
    string1= string1.lower()
    string2= string2.lower()
    if sorted(string1)==sorted(string2):
        return "Anagram"
    else:
        return "Not Anagram"
    
string1= "Listen"
string2="Silent"
res= anagram_checking(string1,string2)
print(res)