def change(arr):
    caps=""
    for i in arr:
        if i.isupper() == True:
            caps+= i.lower()            
        else:
            caps+= i.upper()

    return caps
    
arr="GeekforgEEks"
result= change(arr)
print(result)
