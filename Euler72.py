import math

def fractions(num):
    count = 0
    for i in range(1, num):
        if math.gcd(i, num) == 1:
            count += 1
    return count

def allFractions():
    total = 0
    for i in range(2, 1000001):
        total += fractions(i)
        print(i)
    return total

print(allFractions())
