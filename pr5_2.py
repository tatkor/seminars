# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
filetxt = open('pr_5.txt', 'r')

def coder_s(l1,l2):             # ф- ия для объединия двух списков в список кортежей
    l = list(zip(l1, l2))
    return l

def max_s(s):               # проверка на нулевую строку
    if len(s)==0:
        return 0

    c = s[0]            # начинаем c нулевого символа
    max_s = 0
    cur_s = 0
    val = []
    ar = [c]
    for x in s:  # цикл , для каждого символа в строке
        if x == c:
            cur_s += 1
        else:
            max_s = max(max_s, cur_s)
            val.append(cur_s)
            ar.append(x)
            cur_s = 1
            c = x              # рассмотрим новый символ
    max_s = max(max_s, cur_s)  # после окончания цикла - обновляем max_s
    val.append(cur_s)
    a = coder_s(ar,val)
    return a

#st = 'fffffjjjllnk'
#max_s(st)
for line in filetxt:
    max_s(line)
    print(line)

res = max_s(line)       # получившийся кортеж заносим в переменную res
print(res)
out = (f'{res[0][0]}*{res[0][1]}+{res[1][0]}*{res[1][1]}+{res[2][0]}*{res[2][1]}+{res[3][0]}*{res[3][1]}+{res[4][0]}*{res[4][1]}')
print(out)               # печать закодированной строки

with open ('pr_5out.txt','w') as f_out:      # запись закодированной строки в файл
    f_out.write(out)
filetxt.close()
exit()


















