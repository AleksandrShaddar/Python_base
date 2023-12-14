# numb_1 = int(input("Введите первое число: "))
# numb_2 = int(input("Введите второе число: "))


# Напишите функцию print_operation_table(operation, num_rows, num_columns), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.


def print_operation_table(operation, num_rows = 9, num_columns = 9):
    if num_rows < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
    else:
        for i in range(1, num_rows + 1):
            print(i, end=' ')
            for j in range(1, num_columns + 1):
                print(operation(i, j), end=' ')
            print('\t')
        return operation(num_rows, num_columns)
    
 
# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#     row = [i for i in range(1, num_rows + 1)]
#     colum = [i for i in range(1, num_columns + 1)]    
#     for i in row:
#         for j in colum:
#             print(operation(i, j), ' ', end='')
#         print('')

print_operation_table(lambda x, y: x + y, 7, 7)