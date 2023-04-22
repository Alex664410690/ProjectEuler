import math
def IsPrime(p):
    if p == 1:
        return False
    prime = True
    for j in range(2, math.isqrt(p) + 1):
        if (p / j).is_integer() == True:
            prime = False
    return prime

found = False
n = 13120
while found == False:
    corners = [1, 3]
    n += 2
    for i in range(1, n):
        for j in range(2):
             corners.append(corners[-1] + i + 1)
    count = 0
    print(corners)
    for i in corners:
        if IsPrime(i) == True:
            count += 1
    print(count / len(corners))
    if count / len(corners) < 0.1:
        print(2 * n - 1)
        found = True
