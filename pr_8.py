# Создаем и заполняем БД "sql_my_db.db"  - ,база приложена в файле, программа рабочая
import sqlite3
import traceback  #  выводим трассировку, когда в  коде появляется ошибка
import sys

try:          # Создадим таблицу INSTRUCTOR в нашей БД: ( проверяем, если она не создана)
    sqlite_connection = sqlite3.connect('sql_my_db.db')
    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS INSTRUCTOR (
                                    ins_id integer PRIMARY KEY NOT NULL,
    	                            lastname varchar(30) NOT NULL,
    	                            firstname varchar(30) NOT NULL,
    	                            city varchar(20),
                                    country char(2)
    	                            );'''

    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблица SQLite создана")

                # Если хотим добавить строки в таблицу:
                #**************************************
    #sqlite_insert_query = '''insert into INSTRUCTOR VALUES
                        #(1,'Ahuja','Rav','Toronto', 'CA');'''

                        #(2, 'Chong', 'Raul', 'Toronto', 'CA'),
                        #(3, 'Vasudevan', 'Hima', 'Chicago', 'US');
                        #(4, 'Smitt', 'Nik', 'Monreal', 'Cn')

    #count = cursor.execute(sqlite_insert_query)
    #sqlite_connection.commit()

            # Для удаления строк используем SQL команду - DELETE:
            #***************************************************
    #sqlite_delete_query = '''DELETE from INSTRUCTOR
    #                         WHERE ins_id = 5;'''

    #count = cursor.execute(sqlite_delete_query)
    #sqlite_connection.commit()
    #print("Запись успешно удалена из таблицы INSTRUCTOR ", count)

                 # Выборка всех записей из БД
                 # Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис:
    cursor.execute("SELECT *  FROM INSTRUCTOR")

    results = cursor.fetchall()
    print(results)        # Получаем результат сделанного запроса

    cursor.close()

except sqlite3.Error as error:
    #print("Ошибка при подключении к sqlite", error)
    print("Не удалось вставить данные в таблицу sqlite")
    print("Класс исключения: ", error.__class__)
    print("Исключение", error.args)
    print("Печать подробноcтей исключения SQLite: ")
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")