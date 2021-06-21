# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create a tuple
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

print(fruits, fruits2)

# Single value needs trailing comma
fruits3 = ('Apples',)

# Get value
print(fruits[1])

# Can´t change value
# ∫fruits[0] = 'Pears'

# Delete tuple
#del fruits2

# Get length
print(len(fruits2))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Add duplicate, no error just don´t add it
fruits_set.add('Apples')

# Clear set, leave set empty
fruits_set.clear()

# Delete
del fruits_set

print(fruits_set)
