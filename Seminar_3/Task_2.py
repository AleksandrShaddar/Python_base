# Решение в группах
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]

numbers = [1, 2, 3, 4, 5]

k = 101
# k = k % len(numbers)
# numbers = numbers[-k:]+numbers[:-k]

for i in range(k):
    x = numbers.pop()
    numbers.insert(0, x)
    print(i)
print(numbers)