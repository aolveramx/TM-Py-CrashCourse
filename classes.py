# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object
# constructor: is a function that runs when you instantiate an object for a class
# you can overwrite father class methods when extends that class

# Create a class
class User:
  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age

  def greeting(self):
    return(f'My name is {self.name} and I am {self.age}')

  def has_birthday(self):
    self.age += 1

# Extend class
class Customer(User): 
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0

  def set_balance(self, balance):
    self.balance = balance
    
  def greeting(self):
    return(f'My name is {self.name} and I am {self.age} and my balance is {self.balance}' )

# Init user object
ari = User('ari olvera', 'ari@me.com', 28)
# Init customer
mau = Customer('Mau Rey', 'm@m.com', 25)

mau.set_balance(500)
print(mau.greeting())

# print(type(ari))
# print(ari.name)
# print(ari.greeting())
ari.has_birthday()
print(ari.greeting())