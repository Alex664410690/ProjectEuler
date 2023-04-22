import math
import time

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def list():
    lst = []
    for i in range(2, 4000):
        if prime(i):
            lst.append(i)
    return lst
t = time.perf_counter()
lst = list()
check = False
biggest = 0
length = 0
for i in range(len(lst)):
    for j in range(i):
        list = lst[j:i]
        s = sum(list)
        if s > 1000000:
            check = True
            break
        l = len(list)
        if l > length and prime(s):
            biggest = s
            length = l
    if check:
        break
print(biggest)
print(time.perf_counter() - t)
    
