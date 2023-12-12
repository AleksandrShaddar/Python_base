# Общее обсуждение
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes    

numb = int(input("Ведите число: "))

def prost(x, d = 2):
    if d**2 > x or x == 2:
        return True
    elif x % d == 0:
        return False           
    return prost(x, d + 1)   
    
print(prost(numb))