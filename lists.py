############ Lists in python ##############
# Keep a list of objects ny INDEX

# To declare a list use []. Separate objects using ,
# lists AKA arrays

crazy_x_landlord = ['Jane', 'Mike', 'Cruela Deville']

print(crazy_x_landlord)
print(type(crazy_x_landlord))

# How do we access a list?
#       with an index

print(crazy_x_landlord[1])
print(crazy_x_landlord[-1])

# Edit an entry: use an index and re assign
# Example: change Mike to mike tyson

crazy_x_landlord[1] = 'Mike Tyson'
print(crazy_x_landlord)

# Adding to a list - Use append
#       Add Yuriy to the list

crazy_x_landlord.append('Yuriy')
print(crazy_x_landlord)

# removing something form a list - use .pop()
#       lets remove Jane
crazy_x_landlord.pop(0)
print(crazy_x_landlord)

# Lists can contain anything. Any objects
#   they can contain string, int, objcts, lists, dictionary

combined_list = [1, '10', 'ten', True, crazy_x_landlord]

# List slicing:
#   is used to manage lists

# prints from third index to the end
print(combined_list[3:])

# prints from 3rd index to the start
# but not inclusive of the last
print(combined_list[:3])

# prints from specified index until specified index
# but not inclusive of the last
print(combined_list[0:3])

# Skips slicing - uses :: and returns from the first index
# and skips every nth index on: [x::n]
print(combined_list[0::3])

########## TUPLES - Immutable lists ############
# behave the same way, accessed via index, defined with ()
mortal_enemies = ('HELLO KITTY', 'SAILOR MOON', 'CAPTAIN AMERICA', 'EYEPATCH MORTY')

print(type(mortal_enemies))

mortal_enemies[1] = 'Goku'
