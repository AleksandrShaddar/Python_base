# Решение в группах
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6

numbers = [1, 1, 2, 0, -1, 3, 4, 4]

# uniq = set(numbers)
# print(len(set(numbers)))

# или
lst_1 = []
for i in numbers:
    # if numbers.count(i) > 1:
    #     # numbers.remove(i)
    if i not in lst_1:
        lst_1.append(i)

print(len(lst_1))
