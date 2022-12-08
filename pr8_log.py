import sqlite3
import traceback  # выводим трассировку, когда в  коде появляется ошибка
import sys
import pr8_interface as usi

def loger():

        #print("Ошибка при подключении к sqlite", error)
        # print("Не удалось вставить данные в таблицу sqlite")
        print("Класс исключения: ", error.__class__)
        print("Исключение", error.args)
        print("Печать подробноcтей исключения SQLite: ")
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))