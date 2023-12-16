def copy_user(phone_book, last_name):
    for d in phone_book:
        for v in d.values():
            if v == last_name:                
                return d             
    return {}    