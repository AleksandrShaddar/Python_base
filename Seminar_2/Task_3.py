

days = int(input("Введите кол-во дней наблюдения: "))
temps = []
above_0 = 0

while days > 0:
    t = int(input(f'Температура {days}го дня: '))
    temps.append(t)
    days -= 1
    
snowbreak = 0

for t in temps:
    if t > 0:
        above_0 +=1        
        if above_0 > snowbreak:
            snowbreak += 1            
        else:
            continue
    else:
        above_0 = 0  

print(snowbreak if snowbreak > 0 else "Оттепели не наблюдалось")