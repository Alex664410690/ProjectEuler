import math

primes = [2,3,5]
for i in range(6,2000000):
    prime = True
    n = math.sqrt(i)
    for j in primes:
        if j <= n and i % j == 0:
            prime = False
    if prime == True:
        primes.append(i)
        print(i)
print(sum(primes))

