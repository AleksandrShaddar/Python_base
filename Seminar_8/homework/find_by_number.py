def find_by_number(phone_book, number):
    for d in phone_book:
        for v in d.values():
            if v == number:
                message = f"Телефон {number} принадлежит абоненту : {d['Фамилия']} {d['Имя']}"   
                return message
            else:
                message = f'Абонента с номером {number} нет в справочнике'
    return message