#20. Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

def get_list_from_input(n):
    str_list = [''] * n
    print(str_list)
    for i in range(n):
        str_list[i] = input(f'Input row {i + 1}: ')
        return str_list

try:
    n = int(input('Input number of rows: '))
except ValueError as ex:
    print('Input natural number!')
    exit(ex)

new_list = get_list_from_input(n)

try:
    num = int(input('Input natural number: '))
except ValueError as ex:
    print('Input natural number!')
    exit(ex)

if str(num) in new_list:   # номер, который определяем конвертируем в строку и ищем в new_list
    print(f'Number {num} is found in the list')
else:
    print(f'Number {num} is not found in the list')
