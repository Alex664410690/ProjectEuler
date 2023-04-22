def single(x):
    if x == 1 or x == 2 or x == 6:
        return 3
    elif x == 4 or x == 5 or x == 9:
        return 4
    elif x == 0:
        return 0
    else:
        return 5

def tens(x, y):
    if x == 1:
        if y == 0 or y == 1 or y == 2 or y == 3 or y == 5:
            return 3
        else:
            return 4
    elif x == 2 or x == 3 or x == 4 or x == 8 or x == 9:
        return 6
    elif x == 5 or x == 6:
        return 5
    elif x == 0:
        return 0
    else:
        return 7

total = 0
for i in range (1, 1000):
    print(f"i: {i}")
    temp = total
    total += single(int(str(i)[-1]))
    if len(str(i)) > 1:
        total += tens(int(str(i)[-2]), int(str(i)[-1]))
    if len(str(i)) > 2:
        total += single(int(str(i)[0]))
        if str(i)[-2] == "0" and str(i)[-1] == "0":
            total += 7
        else:
            total += 10
    print(total - temp)
print(total + 11)
