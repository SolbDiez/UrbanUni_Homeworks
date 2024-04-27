immutable_var = (1, 2, True, 'tuple')
print(immutable_var)

# После того как кортеж создан, в него нельзя добавлять элементы, а также изменять их или удалять.
# immutable_var[0] = 100
# print(immutable_var)
# TypeError: 'tuple' object does not support item assignment

mutable_list = list(immutable_var)
mutable_list[0] = 100
print(mutable_list)
