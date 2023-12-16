def find_by_lastname(phone_book, last_name):
    for d in phone_book:
        for v in d.values():
            if v == last_name:                
                message = f"Телефон по запросу {last_name}: {d['Телефон']}"   
                return message             
            else:
                message = f'Абонента {last_name} нет в справочнике'
    return message