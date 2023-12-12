numbers = int(input("Введите длину чисел фибоначи: "))
numb = int(input("Введите искомое число: "))

fibonachi = [0, 1]

while numbers > 2:
    f = fibonachi[-1] + fibonachi[-2]
    fibonachi.append(f)
    numbers -=1

print(fibonachi)
print((fibonachi.index(numb) + 1) if numb in fibonachi else -1)