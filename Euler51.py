import math
def IsPrime(p):
    prime = True
    for j in range(2, math.isqrt(p) + 1):
        if (p / j).is_integer() == True:
            prime = False
    return prime

value = 121310
while True:
    print(value)
    value += 1
    for i in range(len(str(value))):
        for j in range(len(str(value))):
            for k in range(len(str(value))):
                count = 0
                for z in range(10):
                    temp = []
                    for x in str(value):
                        temp.append(x)
                    temp[i] = temp[j] = temp[k] = str(z)
                    temp = int("".join(temp))
                    if IsPrime(temp):
                        count += 1
                if count == 8:
                    break
print(value)



