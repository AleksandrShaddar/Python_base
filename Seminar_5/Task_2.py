# Решение в группах
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). 
# Требуется найти N-е число Фибоначчи
# Input: 7 Output: 21

# number = int(input("Введите число: "))
number = 7

def fibonacci(numb):
    if numb in [1,2]:
        return 1
    return fibonacci(numb - 1) + fibonacci(numb - 2)

print(fibonacci(number))

list_1 = []
for i in range(1, number + 1):
    list_1.append(fibonacci(i))
print(list_1)
