import math

def primes():
    p = []
    for i in range(2, 7500):
        check = True
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                check = False
            if not check:
                break
        if check:
            p.append(i)
    return p


def primePowerTriples():
    prime = primes()
    i = j = k = 0
    total = prime[i]**2 + prime[j]**3 + prime[k]**4
    lst = []
    while total < 50000000:
        while total < 50000000:
            while total < 50000000:
                if total not in lst:
                    lst.append(total)
                i += 1
                total = prime[i]**2 + prime[j]**3 + prime[k]**4
            j += 1
            i = 0
            print(f"{j}, {k}")
            total = prime[i]**2 + prime[j]**3 + prime[k]**4
        k += 1
        j = 0
        total = prime[i]**2 + prime[j]**3 + prime[k]**4
    return len(lst)


print(primePowerTriples())


