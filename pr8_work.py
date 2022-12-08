import sqlite3
import traceback  # выводим трассировку, когда в  коде появляется ошибка
import sys

import pr8_interface
import pr8_log as log


def sql_connection():
    try:
        connection = sqlite3.connect('sql_py.db')
        print("База данных подключена к SQLite")
        return connection
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
        log.loger()


def create_table(connection):
    try:

        cursor = connection.cursor()
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS INSTRUCTOR (
                                    ins_id integer PRIMARY KEY NOT NULL,
    	                            lastname varchar(30) NOT NULL,
    	                            firstname varchar(30) NOT NULL,
    	                            city varchar(20),
                                    country char(2)
    	                            );'''

        cursor.execute(sqlite_create_table_query)
        connection.commit()
        return
        print("Таблица SQLite создана")
        cursor.close()
    except:
        print("Такая таблица уже есть - смотри лог")
        log.loger()


def see_table(connection):

    cursor = connection.cursor()
    # Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
    cursor.execute("SELECT *  FROM INSTRUCTOR")

    # Получаем результат сделанного запроса
    results = cursor.fetchall()
    print(f'Печать результата {results}')
    cursor.close()


def add_info(connection):
    cursor = connection.cursor()
    sqlite_insert_query = '''insert into INSTRUCTOR VALUES
                        (2,'smit','tom','london', 'Br');'''

    count = cursor.execute(sqlite_insert_query)
    connection.commit()
    print("Запись успешно добавлена в таблицу INSTRUCTOR ", count)
    log.loger()
    cursor.close()


def delete_info(connection):
    cursor = connection.cursor()
    sqlite_delete_query = '''delete from INSTRUCTOR
                                 WHERE ins_id = 1;'''

    count = cursor.execute(sqlite_delete_query)
    connection.commit()
    print("Запись успешно  удалена из  таблицы INSTRUCTOR ", count)
    log.loger()
    cursor.close()
