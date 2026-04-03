class Person:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname

  def printname(self):
    print(self.firstname , self.lastname)

x = Person("Ranjan", "Kumar")
x.printname()

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("ravi", "Naik")
x.printname()

# Adding the __init__ function
# If we create a new __init__ function in child class then the __init__ function from parent class is no longer inherited because the child class __ init__ function overrides the parent's __init__ function

#super() function
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  
  def welcome(self):
    print("Welcome", self.firstname , self.lastname, "to the class of", self.graduationyear)

x = Student("Virat", "Kholi", 2026)
x.welcome()
