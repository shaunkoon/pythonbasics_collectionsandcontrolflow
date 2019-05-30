# Here we iterate over nested lists and/or dictionaries

list_data = [1, 2, 3]
embeded_list = [[1, 2, 3], [7, 8, 9]]
dict_data = {
    1: {
        'name': 'James',
        'money': '£30000'
    },
    2: {
        'name': 'Isabella',
        'money': '£300001'
    },
    3: {
        'name': 'Philipe',
        'money': '£3000'
    },
}

print(dict_data)


for data in embeded_list:
    print(data)
    for embeded_data in data:
        print(embeded_data)

for key in dict_data:
    hash = dict_data[key]
    print(hash)
    for key_nd in hash:
        print(key_nd, hash[key_nd])
