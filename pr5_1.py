#  На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять
#  первому игроку, чтобы забрать все конфеты у своего конкурента?
import random

def rnd():
    return random.randint(1,28)

def my_f (n):                    #  (я - первый игрок)
    if n % 29 == 0:
        my_hod = 28
        n = n - my_hod
    else:
        my_hod = n % 29
        n = n - my_hod
    return n

def bot_f(n):
    bot_hod = rnd()
    n = n - bot_hod
    return n

num = 2021
bot_hod = 0
n = my_f(num)
print(n, 'остаток после моего хода')
my_hod = n % 29
konf = num - n

while n > 0:
    n = bot_f(n)
    bot_hod +=1
    print('ход бота №', bot_hod, n,'осталось,')   # ход бота , остаток
    if n > 0:
        m = my_f(n)
        konf += (n-m)
        my_hod += 1
        n = m
        print('Мой ход №', my_hod, n,' осталось,', 'конфет взяла ',konf)

else:
    print('Конфет больше нет!')

