def GetDigits(num):
    lst = list(str(num))
    lst.sort()
    return lst
found = False
i = 0
while found == False:
    found = True
    i += 1
    print(i)
    test = GetDigits(i)
    for j in range(2,7):
        if GetDigits(j*i) != test:
            found = False
            break