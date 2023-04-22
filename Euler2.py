under = True
first = 1
second = 2
total = 2
while under == True:
    if (first + second)%2 == 0:
        total = total + first + second
    first, second = second, first + second
    if first + second > 4000000:
        under = False
print(total)
