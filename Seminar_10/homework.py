# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

data.head()  # Вывод первых 5 строк дата фрейма

# Для перевода в one hot вид без использования функции get_dummies() потребуется создать 2 дополнительные колонки, так как всего 2 значения human и robot
data.loc[data['whoAmI'] == 'robot', 'robot'] = '1'  # Создание колонки robot и заполение строк '1' при выполенении условия
data.loc[data['whoAmI'] == 'human', 'human'] = '1'  # Аналогично для колонки human (см. выше)
data.loc[data['whoAmI'] == 'robot', 'human'] = '0'  # Заполение строк '0' в колонке human при выполенении условия 
data.loc[data['whoAmI'] == 'human', 'robot'] = '0'  # Аналогично для колонки robot (см. выше)

# Первый вариант one hot вида
data[['robot', 'human']]  # Вывод столбцов robot и human (сформированных и заполненных выше)

# Второй вариант one hot вида
data.drop('whoAmI', axis = 1)  # drop() возвращает фрейм данных без удаленного столбца, (axis = 1 для столбца, 0 - для строки)