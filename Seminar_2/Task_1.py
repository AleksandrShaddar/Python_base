n = int(input("Введите число: "))

factorial = 1

while n > 0:
    factorial *= n
    n -= 1

print(factorial)