immutable_var = 'tea', 'ale', 0, 5, True
print(immutable_var)
print(type(immutable_var))
#immutable_var [2] = 10
#TypeError: 'tuple' object does not support item assignment

mutable_list = ['tea', 'ale', 0, 5, True]
print(mutable_list)
print(type(mutable_list))
mutable_list [2] = 10
mutable_list.append(5.5)
print(mutable_list)