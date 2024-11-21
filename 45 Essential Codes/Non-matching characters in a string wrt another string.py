def check_string(string1, string2):
    string2=set(string2)
    extra=[]

    for i in string1:
        if i not in string2:
            extra.append(i)

    return set(extra)

string1="abcde"
string2="acd"
res= check_string(string1,string2)
print(res)
