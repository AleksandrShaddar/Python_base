def show_menu():
    print('1. Распечатать справочник',
        '2. Найти телефон по фамилии',
        '3. Изменить номер телефона',
        '4. Удалить запись',
        '5. Найти абонента по номеру телефона',
        '6. Добавить абонента в справочник',
        '7. Закончить работу', sep = '\n')
    choice = int(input("Выберите требуемое действие: "))
    return choice

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            record = dict(zip(fields, line.split(', ')))
            phone_book.append(record)
    return phone_book

def work_with_phonebook():

    choice = show_menu()

    phone_book = read_txt('Seminar_8/homework/phonebook.txt')

    while (choice != 7):
        if choice == 1:
            for i in phone_book:
                print(i)            
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('Введите фамилию изменяемого абонента: ')
            new_number = input('Введите новый номер телефона: ')
            print(change_number(phone_book, last_name, new_number))
            write_txt('Seminar_8/homework/phonebook.txt', phone_book)
        elif choice == 4:
            lastname = input('Введите фамилию удаляемого абонента: ')
            print(delete_by_lastname(phone_book, lastname))
            write_txt('Seminar_8/homework/phonebook.txt', phone_book)
        elif choice == 5:
            number = input('Введите номер искомого абонента: ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            print("Заполните следующие данные: ")            
            add_user(phone_book)
            write_txt('Seminar_8/homework/phonebook.txt', phone_book)
            print("Новый абонент добавлен!")
        elif choice > 7 or choice == 0:        
            print("Выберете действие из перечня!")
        choice = show_menu()
        
def change_number(phone_book, last_name, new_number):
    for d in phone_book:
        for v in d.values():
            if v == last_name:
                d['Телефон'] = new_number
                message = f"Телефон абонента {last_name} изменен!"  
                return message
            else:
                message = f'Абонента {last_name} нет в справочнике'
    return message



def delete_by_lastname(phone_book, lastname):
    for d in phone_book:
        for v in d.values():
            if v == lastname:
                data = phone_book.remove(d)
                message = f"Абонент {lastname} удален из справочника!"  
                return message
            else:
                message = f'Абонента {lastname} нет в справочнике'
    return message


def add_user(phone_book):
    last_name = input("Введите фамилию нового абонента: ")
    name = input("Введите имя нового абонента: ")
    number = input("Введите номер нового абонента: ")
    des = input("Введите информацию о новом абоненте: ")
    new_user = {'Фамилия': last_name, 'Имя': name, 'Телефон': number, 'Описание': des}
    phone_book.append(new_user)
    return phone_book

def find_by_number(phone_book, number):
    for d in phone_book:
        for v in d.values():
            if v == number:
                message = f"Телефон {number} принадлежит абоненту : {d['Фамилия']} {d['Имя']}"   
                return message
            else:
                message = f'Абонента с номером {number} нет в справочнике'
    return message


def find_by_lastname(phone_book, last_name):
    for d in phone_book:
        for v in d.values():
            if v == last_name:                
                message = f"Телефон по запросу {last_name}: {d['Телефон']}"   
                return message             
            else:
                message = f'Абонента {last_name} нет в справочнике'
    return message

def write_txt(filename, phone_book):
    with open(filename,'w', encoding='utf-8') as f:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s += v + ', '
            f.write(f'{s[:-2]}\n')

work_with_phonebook()
