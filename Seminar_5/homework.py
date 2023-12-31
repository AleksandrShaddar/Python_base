# Задача 1.
# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.
# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8 

def pow_numb(a, b):
    if b == 0:
        return 1
    return a*pow_numb(a, b-1)

print(pow_numb(3, 5))

# или 

def f(a, b):
  if b == 0:
    return 1
  return f(a, b - 1) * a

# Задача 2.
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# Функция не должна ничего выводить, только возвращать значение.

# Пример:
# sum(2, 2)
#  4

def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)

print(sum(2, 7))

# или

def sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return sum(a + 1, b - 1)