from numpy import random

x = random.randint(100)

print(x)

# Generate a random float from 0 to 1:

y = random.rand()
print(y)

# Generate a 1-D array containing 5 random integers from 0 to 100:
z = random.randint(100, size = 5)
print(z)

# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
a = random.randint(100, size = (3, 5 ))

print(a)

# Generate a 1-D array containing 5 random floats:
b = random.rand(5)

print(b)

# Generate a 2-D array with 3 rows, each row containing 5 random numbers:
c = random.rand(3, 5)

print(c)

# Return one of the values in an array:
d = random.choice([1, 2, 3, 4,5],  size=(3, 5))

print(d)