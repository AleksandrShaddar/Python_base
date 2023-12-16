def write_txt(filename, phone_book):
    with open(filename,'w', encoding='utf-8') as f:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s += v + ', '
            f.write(f'{s[:-2]}\n')