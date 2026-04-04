# Create a private class property named __age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age
  
  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Ranjan", 21)
print(p1.name)
print(p1.get_age()) # Private properties cannot be accessed directly from outside the class.  access private property we can use getter method

p1.set_age(46)
print(p1.get_age())

# Example

class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else :
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade
  
  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"
    
std = Student("Ranjan")
std.set_grade(35)
print(std.get_grade())
print(std.get_status())

#protected properties

class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary

p1 = Person("Ranjan", "100000")
print(p1.name)
print(p1._salary) # we can access but we shouldn't 

#private methods

class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):
    if not isinstance(num, (int, float)):
      return False
    return True
  
  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid Number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)

#Name Mangling

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

p1 = Person("Ranjan", 30)
print(p1._Person__age)



