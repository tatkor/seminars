#задача 1. Задайте натуральное число N. Напишите программу, которая составит
#список простых множителей числа N.

n = 20                 # для натуральных чисел от 2-х!
prost = []
for i in range(2, n+1):
    while n % i == 0:
        if n % i == 0:
            prost.append(i)
            n = n//i


print(prost, 'множители числа')

