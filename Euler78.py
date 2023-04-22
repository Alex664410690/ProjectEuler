def coins(l, c, p):
    if len(l) == 2:
        return 1
    for i in range(1, len(l) - 1):
        if p < len(l) - 1:
            l[p] += l.pop(-1)
        c += coins(l, c, p+1)
    return c
print(coins([0 for x in range(5)], 1, 0))