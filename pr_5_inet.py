# Задача на подсчет max значения символов, встречающихся ПОДРЯД в строке!
def max_s(s):
    if len(s)==0:
        return 0

    c = s[0]  # символ с которого мы начинаем
    max_s = 0
    cur_s = 0
    val =[]
    ar=[c]
    for x in s:  # цикл , для каждого символа в строке
        if x == c:
            cur_s += 1
        else:
            max_s = max(max_s, cur_s)
            val.append(cur_s)
            ar.append(x)
            cur_s = 1
            c = x    # рассмотрим новый символ
        #print(x, cur_s)

    max_s = max(max_s, cur_s)  # после окончания цикла - обновляем max_s
    val.append(cur_s)
    print(max_s)

st = 'fffffjjjllnk'
max_s(st)


