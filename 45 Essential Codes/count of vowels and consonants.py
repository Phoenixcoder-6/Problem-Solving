def get_counts(string1):
    string2=['a','e','i','o','u','A','E','I','O','U']
    vowels=[]
    consonants=[]
    for i in string1:
        if i in string2:
            vowels.append(i)
        else:
            consonants.append(i)
    
    return len(vowels),len(consonants)


string1="Ankita"

res1,res2= get_counts(string1)
print("Vowels are:",res1,"Consonants are:",res2)