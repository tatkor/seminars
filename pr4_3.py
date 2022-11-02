# задача 3. Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и записать
# в файл многочлен степени k.  - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def rnd():
    return random.randint(0, 101)

def create_mn(k):
    lst = [rnd() for i in range(k + 1)]
    return lst

koef = create_mn(2)     # Для многочлена во второй степени
print(koef)

if koef[0]==0:
    print(f'{koef[1]} * x + {koef[2]} = 0')
elif koef[1]==0:
    print(f'{koef[0]} * x**2 + {koef[2]} = 0')
elif koef[2]==0:
    print(f'{koef[0]} * x**2  + {koef[1]} * x = 0')
else:
    print(f'{koef[0]} * x**2  + {koef[1]} * x + {koef[2]} = 0')