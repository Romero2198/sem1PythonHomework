a = int(input('Введите число дня недели от 1 до 7: '))
if (a >= 1) and (a <= 5):
    print(f'{a} -> нет')
elif (a == 6) or (a == 7):
    print(f'{a} -> да')
else:
    print('Введите число от 1 до 7')