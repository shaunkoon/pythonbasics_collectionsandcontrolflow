# While loops
#   keep iterating until condition is broken
#   or a control flow of IF to break a clause

# syntax
#   while <condition>:
#       #Block of code

age = 0
while age < 18:
    print('Happy Birthday', 'you are', age)
    age += 1

# while iterator with break condition
age = 0
while True:
    print('Happy Birthday', 'you are', age)
    age += 1
    response = input('do you want to continue?')
    if response == 'n':
        break
    elif response == 'y':
        print('okayyyyy')
    elif response == 'egg':
        print('EGGGGGSSSSS OH YEAH')

