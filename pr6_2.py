# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
def mult(x,y):
    return x*y

def sub(x,y):
    return x-y

def divi(x,y):
    return x/y

def sum(x,y):
    return x+y

def enum_sum(str1):
    for c, i in enumerate(str1):
        k = (str1[c])
        if k in "+":
            a = int(str1[c - 1])
            b = int(str1[c + 1])
            res = sum(a, b)
            #print(res)
            str1[c - 1] = res
            i = str1.index(k)
            #print(str1[:i] , i)
            str_new = str1[:i]
            return str_new

def enumer(str1):
    for c, i in enumerate(str1):
        k = (str1[c])
        if k in "*":
            a = int(str1[c - 1])
            b = int(str1[c + 1])
            res = mult(a, b)
            str1[c - 1] = res
            i = str1.index(k)
            str_new = str1[:i]
            return str_new

str = '1+2*3'
print(type(str), str)
l_str = list(str)
print(enumer(l_str))
r = print(enum_sum(l_str))
