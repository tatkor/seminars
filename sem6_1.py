# Задача 1. Создайте программу для игры в "Крестики-нолики".

def creat_xo():
    table = []
    for i in range(3):
        table_c= []
        for j in range(3):
            table_c.append(' - ')
        table.append(table_c)
    return table

def print_tabl(array):
    for i in range(3):
        print("".join(array[i]))

table = creat_xo()
char = 'X'
hod = 0
while hod <= 9:
    print_tabl(table)
    b = int(input('Введите строку '))
    a = int(input('Введите столбец '))
    hod += 1
    table[a-1][b-1]= char
    if char == 'X':
        char = '0'
    else:
        char = 'X'


#print_tabl(creat_xo())
