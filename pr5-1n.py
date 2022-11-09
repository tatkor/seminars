import random   # с интелектуальным ботом- не интересно получается, все одно и тоже)

def rnd_hod():
    return random.randint(0,1)

def rnd():
    return random.randint(1,28)

def my_f (n):                    #  ( первый игрок)
    if n % 29 == 0:
        my_hod = 28
        n = n - my_hod
    else:
        my_hod = n % 29
        n = n - my_hod
    return n

def bot_f(n):                    # бот, наделенный логикой
    if n % 29 == 0:
        bot_hod = 28
        n = n - bot_hod
    else:
        bot_hod = n % 29
        n = n - bot_hod
    return n

num = 2021
bot_hod = 0
my_hod = rnd_hod()
print(my_hod)
konf = 0
if my_hod == 0:
    print('Первый ход бота!')
    while num > 0:
        n = bot_f(num)
        bot_hod +=1
        num = n
        print('ход бота №', bot_hod, num,'осталось,')   # ход бота , остаток
        if num > 0:
            m = my_f(num)
            konf += (num-m)
            my_hod += 1
            num = m
            print('Мой ход №', my_hod, num,' осталось,', 'конфет у меня ',konf)

else:
    print('Первый мой ход!')
    while num > 0:
        n = my_f(num)
        konf += (num-n)
        num = n
        print('Мой ход №', my_hod, num,' осталось,', 'конфет у меня',konf)
        my_hod += 1
        if num > 0:
            n = bot_f(num)
            bot_hod += 1
            num = n
            print('ход бота №', bot_hod, num, 'осталось,')

print('Конфет больше нет!')

