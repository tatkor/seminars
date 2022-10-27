#Задача 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
def funk_max_min(arr):

    max_val = 0
    min_val = round((arr[0] % 1),2)   # назначаем первому элементу массива
    for i in range(len(arr)):
        res = round((arr[0] % 1),2)    # округляем до 2-х знаков
        if arr[i] % 1 != 0 and arr[i] % 1 > max_val:    # проверяем условие на максимальное значение и далее на мин
            max_val = round(arr[i] % 1, 2)
        elif arr[i] % 1 != 0 and arr[i] % 1 < min_val:
            min_val = round(arr[i] % 1, 2)
        else:
            print('  ')
    print(max_val - min_val)            # находим разность макс и мин значений

lst = [1.1, 1.2, 3.1, 5, 10.01]
print(lst)
funk_max_min(lst)






