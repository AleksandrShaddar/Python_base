# Задача 1.
# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, чтобы все монетки лежали одной и той же стороной вверх.
# Входные данные:
# На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, и равно 1, если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.
# Выходные данные:
# Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.

coins = [0, 1, 1, 1, 0, 1]

zero = coins.count(0)
one = coins.count(1)

if zero >= one:
    print(one)
else:
    print(zero)

# или

count_zero = 0
count_one = 0

for coin in coins:
    if coin == 0:
        count_zero += 1
    else:
        count_one += 1

if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)    

# Задача 2.
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.

n = 16

for i in range(n):    
    a = 2**i
    if a <= n:
        print(a)

# или 

i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1

# Задача 3.
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.

s = 48
p = 320


first_numb = 0 # число X
second_numb = 0 # число Y

while first_numb <= 1000:
    while second_numb <= 1000:
        if (first_numb + second_numb == s) and (first_numb * second_numb == p) and (first_numb <= second_numb):
            print(first_numb, second_numb)
        second_numb += 1
    first_numb += 1
    second_numb = 0

# или 

solutions = []
for i in range(1, 1001):
    for j in range(1, 1001):
        if s == i + j and p == i * j:
            solutions.append((min(i, j), max(i, j)))
solutions = list(set(solutions))

for solution in solutions:
    print(solution[0], solution[1])