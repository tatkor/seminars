# Задача 4. Напишите программу, которая будет преобразовывать десятичное число
# в двоичное. Нельзя использовать готовые функции. - 45 -> 101101;- 3 -> 11; - 2 -> 10

num = 45   #input("число : ")
bi = []
for i in range(10):
    while num - num/2 > 0:
        print(num, 'num')
        print(num % 2, 'num%2')
        if num % 2 != 0:
            ostat = 1
            num = num // 2
            bi.append(ostat)
        else:
            ostat = 0
            bi.append(ostat)
            num = num // 2
        print(bi[::-1])