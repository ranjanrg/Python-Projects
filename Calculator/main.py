def add(x,y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x ,y):
  return x * y

def divide(x, y):
  return x / y

while True: 
  print("Calculate.....")
  print("I want to..")
  print('''
      1. Add
      2. Subtract
      3. Multiply
      4. Divide
        '''
        )

  try:
    Operation = int(input("Enter the operation to perform from the menu: "))
  except ValueError: 
    print("Need valid input")
    continue

  operations = [1, 2, 3, 4]

  if Operation not in operations:
    print("Invalid Input, Plz try again")
  else:
    try:
      x = int(input("Enter the First Number: "))
      y = int(input("Enter the second Number: "))
    except ValueError:
      print("Invalid Input")
      continue

    if Operation == 1:
      result = add(x, y)
      print(f"Addition of {x} and {y} is {result}")
    elif Operation == 2:
      result = subtract(x, y)
      print(f"Subtraction of {x} and {y} is {result}")
    elif Operation == 3:
      result = multiply(x, y)
      print(f"Multiplication of {x} and {y} is {result}")
    elif Operation == 4:
      if y == 0:
        print("Cannot divide by zero")
      else: 
        result = divide(x, y)
        print(f"Division of {x} and {y} is {result}")

  Next = input("Do you want to continue(Y/N):")
  if Next.lower() == 'n':
    break
  elif Next.lower() == 'y':
    continue
  else:
    print("Invalid choice")
