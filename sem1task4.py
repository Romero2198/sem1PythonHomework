a = int(input('Введите номер координатной четверти:'))
if a == 1:
    print(f'{a} четверть - X = от 1 до ∞, Y = от 1 до ∞')
elif a == 2:
    print(f'{a} четверть - X = от -1 до -∞, Y = от 1 до ∞')
elif a == 3:
    print(f'{a} четверть - X = от -1 до -∞, Y = от -1 до -∞')
elif a == 4:
    print(f'{a} четверть - X = от 1 до ∞, Y = от -1 до -∞')
else:
    print('Введите число от 1 до 4')