# 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# - для k = 8 список будет выглядеть так:
# [-21, 13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]/// Fn = F(n+2)−F(n+1)
def fib(n):
    if n in (1, 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

k = int(input('Введите k  '))
ar = [0,]
for i in range(1, k+1):
     ar.append(fib(i))
     ar.insert(0,(-1) ** (i + 1) * (fib(i)))

print(ar)

