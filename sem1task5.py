from math import sqrt
x1 = int(input('Введите X первой точки: '))
y1 = int(input('Введите Y первой точки: '))
x2 = int(input('Введите X второй точки: '))
y2 = int(input('Введите Y второй точки: '))
distance = round(sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1)), 3)
print(f'A {x1, y1}; B {x2, y2} -> {distance}')
