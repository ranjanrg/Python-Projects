#create a class in python

class MyClass():
  x = 5

# create an object

p1 = MyClass()
print(p1.x)

#use of _init_()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p2 = Person('Ravi', 21)
print(p2.name)
print(p2.age)

p3 = Person('Ranjan', 22)
print(p3.name)
print(p3.age)

#calling a method in with self

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return f"{self.name} Hello"
    
  def welcome(self):
    message = self.greet()
    print(message + "Welcome to our website")

p = Person("rahul")
p.greet()
p.welcome()

#modify class properties value
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p5 = Person('kiran', 23)
print(p5.age)

p5.age = 79
print(p5.age)


#delete properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p6 = Person("Linus", 30)

del p6.age

print(p6.name)


#class properties and object properties
class Person:
  species = "Human" #class property

  def __init__(self, age):
    self.age = age

p8 = Person(21)
p9 = Person(45)
print(p8.species)
print(p9.species)

#modifying class property
class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname)
print(p2.lastname)

#modifying object property in methods of class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    self.age += 1
    return f"Congrats {self.name} is {self.age} year old"
  
p10 = Person('Ranjan', 21)
print(p10.greet())
print(p10.greet())

#__str__()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} is {self.age} year old"

p11 = Person("Emil", 36)
print(p11)

#multiple methods

class Playlist:
  def __init__(self):
    self.songs = []

  def add_song(self,song):
    self.songs.append(song)
    print(f"{song} is added to your playlist")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
    print(f"{song} is removed from the Playlist")

  def show_songs(self):
    for song in self.songs:
      print(song)
      

my_playlist = Playlist()
my_playlist.add_song("Money")
my_playlist.add_song("Sugar")
my_playlist.show_songs()
my_playlist.remove_song("Money")
my_playlist.show_songs()

#delete method
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello!")

p1 = Person("Emil")

del p1.greet

# p1.greet() # This will cause an error


