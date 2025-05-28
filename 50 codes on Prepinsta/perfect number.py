n= int(input("Enter any number:"))
sum=0
for i in range(1,n):
    if (n%i ==0):
        sum+= i
if sum ==n:
    print("Perfect number")
else:
    print("Not a perfect number")