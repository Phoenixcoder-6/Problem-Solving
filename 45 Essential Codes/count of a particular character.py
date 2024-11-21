def find_occurance(string,n):
    count=0
    for i in string:
        if i == n:
            count+=1

    return count

string= "Darjeeling"
letter='e'
res= find_occurance(string,letter)
print("The occurance of",letter,"is:", res)


