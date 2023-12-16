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