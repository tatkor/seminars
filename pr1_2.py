# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений #предикат.
try:
    x, y, z = int(input('Введите x ')), int(input('Введите y ')), int(input('Введите z '))

    v = not x and not y and not z
    w = not (x or y or z)
    if v == w:
        print('Утверждение истинно')
    else:
        print('Утверждение ложно')
except:
    print('Введите целое число')