arr= [2,3,4,67,1,89,90,34]
n= int(input("Enter the position:"))

first_half= sorted(arr[:n])
next_half= sorted(arr[n:],reverse=True)

result= first_half + next_half

print(result)