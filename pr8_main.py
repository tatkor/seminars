import easygui as gui
from easygui import *
import sqlite3
import traceback  # выводим трассировку, когда в  коде появляется ошибка
import sys
import pr8_interface as usi
import pr8_log as log


if __name__ == '__main__':
    usi.working_table()
