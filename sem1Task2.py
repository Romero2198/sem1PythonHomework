def bool_check(x, y ,z):
    left = not(x or y or z)
    right = (not x) and (not y) and (not z)
    if left == right:
        print("True")
    else:
        print("False")
bool_check(0,0,1)
bool_check(0,1,1)
bool_check(1,1,1)
bool_check(1,0,0)
bool_check(1,1,0)
bool_check(0,1,0)
