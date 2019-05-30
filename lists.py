# lists in python
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

