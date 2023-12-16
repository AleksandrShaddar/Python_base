def add_user(phone_book):
    last_name = input("Введите фамилию нового абонента: ")
    name = input("Введите имя нового абонента: ")
    number = input("Введите номер нового абонента: ")
    des = input("Введите информацию о новом абоненте: ")
    new_user = {'Фамилия': last_name, 'Имя': name, 'Телефон': number, 'Описание': des}
    phone_book.append(new_user)
    return phone_book