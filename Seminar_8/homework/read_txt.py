def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            record = dict(zip(fields, line.split(', ')))
            phone_book.append(record)
    return phone_book