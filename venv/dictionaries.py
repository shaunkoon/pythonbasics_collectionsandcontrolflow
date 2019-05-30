######### Dictionaries - Work with keys and values ########

#       They dont use index. They use KEYS
#   You look up keys to get values
#   Keys are unique
#   Dictionaries AKA Hashes or (confusingly) objets in JS

# Defining a dictionary
#   use {}
#   key: value
#       Where key can be a string or a number with ":"
#       at the end
#       Where calue can be any objects (array, dictionaries etc)

crazy_cruella = {
    'name': 'Cruella de Vil',
    'occupation': 'Fashion Designer',
    'address': 'Hell Hall',
    'door_number': 666,
    'skills': ['Skinning', 'Evil laugh']
    }
print(crazy_cruella['skills'])

# How to use dictionary?
#   Use the keys. Inside []
print(crazy_cruella['skills'])

# How to edit a value
#
crazy_cruella['door_number'] = 101
print(crazy_cruella['door_number'])

# Accessing and directly manipulating usong methods
crazy_cruella['skills'].append('Business Skills')
print(crazy_cruella['skills'])

# Adding a new key: values
#      Same as editing - if ti dosent exit it it creates it
crazy_cruella['favourite_colour'] = 'Black and White'
print(crazy_cruella['favourite_colour'])

# Useful methods for dictionaries
#   Getting all the keys out

keys = crazy_cruella.keys()
print(keys)

#   Getting values

values = crazy_cruella.values()
print(values)

# Iterating over a hash/dictionary
#   using a for loop

# When we iterate over a dictionary we get individual keys
for placeholder in crazy_cruella:
    print(placeholder, ":" ,crazy_cruella[placeholder])