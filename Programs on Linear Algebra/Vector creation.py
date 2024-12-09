arr=[]
n= int(input("Enter the number of spaces you want to enter:"))
for i in range(1,n+1):
    value=int(input(f"Enter the value at {i}th position:"))
    arr.append(value)

print("Vector is:", arr)
