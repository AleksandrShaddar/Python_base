def write_new_txt(filename, user):
    with open(filename,'a', encoding='utf-8') as f:
        s = ''
        for v in user.values():
            s += v + ', '
        f.write(f'{s[:-2]}\n')