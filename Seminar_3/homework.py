# Задача 1.
# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.

list_1 = [1, 2, 3, 4, 5]
k = 3

if k in list_1:
    print(list_1.count(k))
else:
    print("Такого элемента нет в списке")

# или

count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)

# Задача 2.
# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

list_1 = [1, 2, 3, 4, 5, 12, 17]
k = 9


if k in list_1:
    print(k)
else:
    counter = 1
    if k > max(list_1):
        while k - counter not in list_1:
            counter += 1
        print(k - counter)
    elif k < min(list_1):
        while k + counter not in list_1:
            counter += 1
        print(k + counter)
    else:
        while k - counter not in list_1:
            counter += 1
        minimal = k - counter  
        counter = 1
        while k + counter not in list_1:
            counter += 1
        maximal = k + counter 
        print(minimal if abs(k - minimal) < abs(k - maximal) else maximal)

# или

m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)

# Задача 3.
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

k = 'ноутбук'

word = k.upper()

eng_points = {
    1:["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"], 
    2:["D", "G"], 3:["B", "C", "M", "P"], 
    4:["F", "H", "V", "W", "Y"], 5:["K"], 
    8:["J", "X"], 
    10:["Q", "Z"]
    }

rus_points = {
    1:["А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"], 
    2:["Д", "К", "Л", "М", "П", "У"], 
    3:["Б", "Г", "Ё", "Ь", "Я"], 
    4:["Й", "Ы"], 
    5:["Ж", "З", "Х", "Ц", "Ч"], 
    8:["Ш", "Э", "Ю"], 
    10:["Ф", "Щ", "Ъ"]
    }

score = 0

for simbol in word:
    for k, v in eng_points.items():
        if simbol in v:
            score += k
    for k, v in rus_points.items():
        if simbol in v:
            score += k
           
print(score)    

# или

points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = k.upper()  # переводим все буквы в верхний регистр
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                count = count + j
    else:
        for j in points_en:
            if i in points_ru[j]:
                count = count + j
print(count)

