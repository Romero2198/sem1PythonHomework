x = int(input('Введите X: '))
y = int(input('Введите Y: '))
if (x > 0) and (y > 0):
    print(f"{x, y} -> 1")
elif (x < 0) and (y > 0):
    print(f"{x, y} -> 2")
elif (x < 0) and (y < 0):
    print(f"{x, y} -> 3")
elif (x > 0) and (y < 0):
    print(f"{x, y} -> 4")
else:
    print("X или Y не могут быть равны 0")