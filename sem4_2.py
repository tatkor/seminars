#2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 ) с помощью математических формул
# нахождения корней квадратного уравнения  D = b^2 - 4*a*c
#если D < 0, корней нет;
#если D = 0, есть один корень;
#если D > 0, есть два различных корня.

a, b, c = map(int,input('Введите a, b, c ').split())

D = b ** 2 - 4 * a * c
print(D)
if D == 0:
    print('есть один корень')
elif D > 0:
    print('есть два различных корня')
else:
    print('корней нет')
