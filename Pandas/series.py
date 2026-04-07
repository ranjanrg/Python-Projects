import pandas as pd

mydataset = [1, 7, 2]

myvar = pd.Series(mydataset, index = ['X', 'Y', 'Z'])

print(myvar)

print(myvar['X'])

# Create a simple Pandas Series from a dictionary:

a = {
  'day1' : 300,
  'day2' : 320,
  'day3' : 400
}

myvar1 = pd.Series(a, index=['day2', 'day3'])

print(myvar1)

# Create a DataFrame from two Series:

data = {
  "calories" : [420, 380, 390],
  "duration" : [50, 40, 45]
}

myvar2 = pd.DataFrame(data)

print(myvar2)
