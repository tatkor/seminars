
import easygui as gui
from easygui import *
import sqlite3
import traceback  # выводим трассировку, когда в  коде появляется ошибка
import sys

import pr8_work as w
import pr8_main
import pr8_log as log


# Эта функция вызывает главное меню графического интерфейса пользователя и предлагает сделать выбор
def working_table():
    connection = sqlite3.connect('sql_py.db')

    message = 'Выберите, что хотите сделать: '
    title = 'Главное меню'
    make = ['Создать таблицу', 'Просмотреть таблицу',
            'Добавить строки в таблицу', 'Удалить строки из таблицы']
    result = choicebox(message, title, make)

    if result == 'Создать таблицу':

        w.create_table(connection)

    elif result == 'Просмотреть таблицу':

        w.see_table(connection)
    elif result == 'Добавить строки в таблицу':
        w.add_info(connection)
    elif result == 'Удалить строки из таблицы':
        w.delete_info(connection)
