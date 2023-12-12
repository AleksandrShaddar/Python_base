# Задача 1.
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

for i in range(len(list_1)):
    if list_1[i] <= max_number and list_1[i] >= min_number:
        print(i)

# или

# for i in range(len(list_1)):
#   if min_number <= list_1[i] <= max_number:
#     print(i)

# Задача 2.
# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент a1 , разность d и количество элементов n будет задано автоматически. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

a1 = 2
d = 3
n = 4

list_1 = []

for i in range(n):
    next_numb = a1 + i*d
    list_1.append(next_numb)
    print(next_numb)

# или

# for i in range(n):
#   print(a1 + i * d)

# Задача 3.

k = 300
for i in range(1, k):
    t = 0
    n = 0
    for x in range(1, i):
        if i % x == 0:
            t += x
    for j in range(1, t):
        if t % j == 0:
            n += j
    if i == n and i < t:
        print(i, t)