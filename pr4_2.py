# задача 2 . Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

lst = [2, 24, 24, 3, 3, 2]

def uniq_list(num):
    ar = set(num)
    uniq = list(ar)
    uniq.sort()
    print(uniq)

uniq_list(lst)

