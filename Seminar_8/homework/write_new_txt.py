def write_new_txt(filename, user):
    with open(filename,'a', encoding='utf-8') as f:
        if len(user) > 0:
            s = ''
            for v in user.values():
                s += v + ', '
            f.write(f'{s[:-2]}\n')
            print(f"Абонент {user['Фамилия']} скопирован!")
        else:
            print('Такого абонента нет в справочнике!')