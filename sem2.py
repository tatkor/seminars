# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов. Для N = 5: 1, -3, 9, -27, 81
#a = 5 #int(input('введите N ')
#ls = []
#n = 5
#for i in range(n):
#	ls.append((-3)**i)

#print(ls)
#_______________
# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
dict = {}
n = 6
for i in range(1,n+1):
	dict[i]=3*i + 1
print(dict)