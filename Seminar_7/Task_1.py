# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))

# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#  print(‘ok’)
# else:
#  print(‘fail’)
# Вывод:
# ok

values = [1, 23, 42, 'asdfg']

transformed_values = list(map(lambda x: x, values))
print(transformed_values)

if values == transformed_values:
    print('ok')
else:
    print('fail')
# Вывод:
# ok