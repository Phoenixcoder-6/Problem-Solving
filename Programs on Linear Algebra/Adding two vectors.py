#Vectors in Linear Algebra

a = [3, 5, -5, 8]
b = [4, 7, 9, -4]

print("Vector a = ", a)
print("Vector b = ", b)

# This is a 4 dimensional vector
# a list in python is a vector in linear algebra

# adding vectors
sum = []
for i in range(len(a)):
    sum.append(a[i] + b[i])

print("Vector Addition = ", sum)
# This is how we can print a vector in python
