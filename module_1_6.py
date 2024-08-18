my_dict = {'ale': 4, 'lager': 5, 'stout': 6}
print(my_dict)
print(my_dict['lager'])
print(my_dict.get('mild', 'Такого ключа нет'))
my_dict['mild'] = 3
my_dict.update({'bock': 7})
del my_dict ['lager']
print(my_dict)

my_set = {1, 2, 3, False, 'water', 2, 5.6, 3, 'water', 5.6}
print(my_set)
my_set.add('ice')
my_set.add((10, 9, 8))
my_set.remove(3)
print(my_set)