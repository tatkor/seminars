# Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
# первое число, второе число и операцию, после чего применяет операцию к введённым числам
# ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div
#def sum(a, b): return a + b
#def dif(a, b): return a - b
#def mult(a, b): return a * b
#def divi(a, b): return a / b
#def mod(a, b): return a % b
#def pow(a, b): return a ** b
#def div(a, b): return a // b

x = float(input('Первое значение '))
val = input('Операция ')
y = float(input('Второе значение '))

if val == '+':
    print(x + y)
elif val == '-':
    print(x - y)
elif val == '*':
    print(x * y)
elif val == '/':
    print(x / y)
elif val == '%':
    print(x % y)
elif val == '**':
    print(x ** y)
elif val == '//':
    print(x // y)
else:
    print('Введите корректную операцию')

# Деление на 0!



