# Функции, лямбда
def mult(a,b):
    return a * b
# 2 варианта записи ф-ии sum:
#def sum(a, b)
#    return a + b

#sum = lambda x, y: x + y

# op - операция с двумя переменными x и y. В качестве аргумента- функция.
def calc(op, x ,y):
    #return op(x * y)
    print(op(x, y))
# добавим нашу лямбду в функцию calc:
calc(lambda x, y: x * y, 4, 5)

