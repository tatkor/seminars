# Timur Islamgulov: 36. Дан список чисел. Создайте список, в который попадают числа,
# описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 2, 8, 12, 3, 4, 1, 7] => [1, 4]

def uniq_list(num):
    ar = set(num)
    uniq = list(ar)
    return uniq

ls = [1, 8, 12, 3, 4, 1, 7]
un = uniq_list(ls)
print(un)
un_min = min(un)
un_val = un_min
for i in range(len(un)):
    if un_val in un:
        un_val += 1
        ar = [un_min, un_val-1]
print(ar)