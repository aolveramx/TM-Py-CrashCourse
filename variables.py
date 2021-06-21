# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x = 1           # int
y = 2.5         # float
name = 'John'   # str
is_cool = True  # bool

# Multiple assignment
a, b, name2, last_name = (1, 2.5, 'Doe', True)

print('Hello')
print(a, b, name2, last_name)

# Basic math
a = x + y
print(a)

print(type(x))

# Casting
x = str(x)
y = int(y)
z = float(a)

print(type(y), z)
