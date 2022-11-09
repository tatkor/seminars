# нет ничего
st = 'fffffjjjllnk'
# все символы, которые повторяются 2 и более раз
{k:v for k, v in Counter(st).items() if v > 1}
# {'а': 5, 'б': 2, 'р': 2}