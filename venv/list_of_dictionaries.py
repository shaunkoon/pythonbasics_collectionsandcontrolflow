# Here we will practice a list of dictionaries

list_evil_ppl = []

crazy_cruella = {
    'name': 'Cruella de Vil',
    'occupation': 'Fashion Designer',
    'address': 'Hell Hall',
    'door_number': 666,
    'skills': ['Skinning', 'Evil laugh']
    }

tmay = {
    'name': 'Theresa May',
    'occupation': 'Unemployed',
    'address': 'Downing Street',
    'door_number': 10,
    'skills': ['Almost Brexit', 'Time management']
    }

thanos = {
    'name': 'Thanos',
    'occupation': 'Tough guy',
    'address': 'Downing Street',
    'door_number': 'n/a',
    'skills': ['splitting the bill', 'finger clicking']
    }

jeff = {
    'name': 'Jeff Bezos',
    'occupation': 'CEO',
    'address': 'America',
    'door_number': '100 billion',
    'skills': ['having money', 'delivery boy']
    }

list_evil_ppl.append(jeff)
list_evil_ppl.append(thanos)
list_evil_ppl.append(crazy_cruella)
list_evil_ppl.append(tmay)

print(len(list_evil_ppl))

#
print(list_evil_ppl[3])

print(list_evil_ppl[3]['address'])

for obj in list_evil_ppl:
    print('name:', obj['name'])