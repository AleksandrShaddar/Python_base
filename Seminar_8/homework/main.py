from add_user import add_user
from change_number import change_number
from delete_by_lastname import delete_by_lastname
from find_by_lastname import find_by_lastname
from find_by_number import find_by_number
from read_txt import read_txt
from show_menu import show_menu
from write_txt import write_txt


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

work_with_phonebook()