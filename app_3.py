#задача 3. Напишите программу, которая принимает на вход координаты точки
#(X и Y), и выдаёт номер четверти плоскости, в которой находится эта точка
#(или на какой оси она находится).
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

x, y = int(input('Введите координаты x= ')), int(input('Введите координаты y= '))
s = (x, y)
#print(s[0], type(s))
if s[0] > 0 and s[1] > 0:
    print('1')
elif s[0] > 0 and s[1] < 0:
    print('4')
elif s[0] < 0 and s[1] < 0:
    print('3')
elif s[0] < 0 and s[1] > 0:
    print('2')
elif s[0] == 0:
    print('ось Y')
elif s[1] == 0:
    print('ось X')
else:
    print('Начало координат')