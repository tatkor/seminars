#3. Задайте список из n чисел последовательности (1+1/N)**N и выведите на экран их сумму.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
#n=6
#ls =[]
#s = 0
#for i in range(1,n+1):
#    s += (1+1/i)**i
#    ls.append(s)
#print(ls)

#4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt
# в одной строке одно число.
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()






