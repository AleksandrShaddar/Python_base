numb = int(input("Введите кол-во арбузов: "))

weight = []

while numb > 0:
    w = int(input("Вес арбуза: "))
    weight.append(w)
    numb -= 1
print(f'Самый большой вес арбуза {max(weight)} кг')
print(f'Самый маленький вес арбуза {min(weight)} кг')