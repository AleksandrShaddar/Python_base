# Найти рекурсией факториал числа

# number = int(input("Введите число: "))
number = 3

def fact(numb):
    if numb <= 1:
        return 1
    return numb * fact(numb - 1)

print(fact(number))