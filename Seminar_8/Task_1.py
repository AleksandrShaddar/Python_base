# Вводится список целых чисел в одну строчку через пробел. 
# Необходимо оставить в нем только двузначные числа. 
# Реализовать программу с использованием функции filter. 
# Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.


# пример - 8 11 0 -23 140 1 => 11 -23 

str1='-8 11 0 -23 140 1'
list_1 = list(map(int, str1.split()))

res = list(filter(lambda x: 10 <= abs(x) <= 99, list_1))

print(*res)

# или

res = list(filter(lambda x: len(x.strip('-')) == 2, str1.split()))

print(*res)