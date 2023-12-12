# Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

words = "a a a b c a a d c d d"
dict_1 = {}

list_1 = words.split()

for i in list_1:
    if i not in dict_1:
        print(i, end=' ')
        # dict_1[i] = 1 
    else:
        print(f'{i}_{dict_1[i]}', end=' ')
        # dict_1[i] += 1
    dict_1[i] = dict_1.get(i, 0) + 1
