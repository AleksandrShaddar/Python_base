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