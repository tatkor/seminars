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

#__3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.___________________________________
Alexander Bashlaev: def lcm(a, b):
for i in range(max(a, b), a * b + 1):
if i % a == 0 and i % b == 0:
return i

def main():
try:
a = int(input('Input number A: '))
b = int(input('Input number B: '))
except ValueError as ex:
print('Input natural number!')
exit(ex)

print(f'LCM({a}, {b}) = {lcm(a, b)}')

if __name__ == '__main__':
main()

#