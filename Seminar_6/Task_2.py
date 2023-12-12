# определить является ли слово полиндромом

word = input("Введите текст: ")

def poli(text):
    if text[0] != text[-1]:
        return False
    elif len(text) <= 2:
        return True
    return poli(text[1:-1])
print(poli(word))