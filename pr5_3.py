# 3.Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Функции FIND и COUNT юзать нельзя.

str = 'абва рывабвгцу квабвваабв'
print(str)
abv = 'абв'

for abv in str:
    if str.index(abv):
        d = str.replace('абв','')

print(d)
