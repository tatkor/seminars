# Задача 1. Создайте программу для игры в "Крестики-нолики".
print("ПРОГРАММА КРЕСТИКИ-НОЛИКИ")
def create_field(field):  # функция отрисовки поля и заполнения его значениями из списка
    for i in range(3):
        print("|",field[0 + i*3], "|", field[1 + i*3], "|", field[2 + i*3], "|")

def check_win(field):     # функция проверки игрового поля с выигрышными комбинациями
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   #print('win_coord = ', win_coord)
   for each in win_coord:
       if field[each[0]] == field[each[1]] == field[each[2]]:
           return field[each[0]]
   return False


count = 0
win = False
field = list(range(1,10))     # список для создания поля ввода
iter = ["X", "O", "X", "O", "X", "O", "X", "O","X"]   # 2-ой список для поочередной вставки в поле хода
create_field(field)
for c, i in enumerate(iter):
    try:                # если введено не число
        k = int(input('Введите номер поля от 1 до 9 '))
        if k in field:
                k = k-1
                field[k] = i
                count += 1
                print(create_field(field))
                if count > 4:   # если счетчик более 4-х, то проверяем выигрышные комбинации
                    tmp = check_win(field)
                    if tmp:
                        print(tmp, "выиграл!", create_field(field))
                        win = True
                        break
                if count == 9:     # Количество возможных ходов
                    print("Ничья!")
                    break
        else:
            k = int(input('Введите номер пустого поля,от 1 до 9:  '))
            if k in field:
                k = k - 1
                field[k] = i
                count += 1
            print(create_field(field))
            continue
    except:
        k = int(input('Введите номер пустого поля,от 1 до 9:  '))
        if k in field:
                k = k-1
                field[k] = i
                count += 1
        print(create_field(field))
        continue

    print(create_field(field))
input("Нажмите Enter для выхода!")

