#21. Напишите программу, которая определит позицию второго вхождения
#строки в списке либо сообщит, что её нет.
#*Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#- список: [], ищем: "123", ответ: -1    Alexander Bashlaev:

def get_list_from_input(n):
    str_list = [''] * n
    for i in range(n):
        str_list[i] = input(f'Input row {i + 1}: ')

        return str_list


def check_string_in_list(l, s):
    count = 0
    for i in range(len(l)):
        if l[i] == s:
            count += 1
            if count == 2:
                return i

    return -1


try:
    n = int(input('Input number of rows: '))
except ValueError as ex:
    print('Input natural number!')
    exit(ex)

new_list = get_list_from_input(n)

str = input('Input string for check: ')

print(check_string_in_list(new_list, str))


