from funcscl import inBase, lastRow, allData, getGifnum, getKeyword, getLink
from funcscl import CreateRequestsTable, CreateIMGTable, Fill_keyword_ids, UpdateLink
from words import data_set

#   Функции для настройки БД
# Создание таблицы images
#CreateIMGTable()

# Создание таблицы запросов
#CreateRequestsTable()

# Вызываем функцию для заполнения столбца keyword
#Fill_keyword_ids(data_set)

# Функция для обновления ссылок на картинки
#UpdateLink('поздоровайся', f'D\sourse\img{i}')
#i=1
#for keyw in data_set.keys():
    #UpdateLink(keyw, f'D\sourse\img{i}')
    #i += 1
#============================================================

#   Функции для ядра ИИ (Андрею)
#   Вставка данных в таблицу
#   inBase(аргумент с номером анимации, аргумент с ключем)
inBase(3, 'представься')

#============================================================

#   Функции для Бэка (Саве)
#   Выводит данные таблицы запросов текстом
lastRow()

#   Кидает все данные из базы в переменную
data = allData()
print(f'Номер анимации = {data[0]}')
print(f'Ключ = {data[1]}')
print(f'Ссылка на картинку = {data[2]}')

#   Возвращает номер анимации в переменную
num = getGifnum()
print('num =', num)

#   Возвращает ключ в переменную
word = getKeyword()
print('word =', word)

#   Возвращает ссылку на картинку в переменную
img_link = getLink()
print('img_link =', img_link)