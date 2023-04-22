import math

primes = [2,3,5]
for i in range(6,200):
    prime = True
    n = math.sqrt(i)
    for j in primes:
        if j <= n and i % j == 0:
            prime = False
    if prime == True:
        primes.append(i)

nums = [1]
for i in range(2, 100):
    nums.append(nums[-1] + i)
for i in nums:
    val = i
    x = 0
    while x < val:
        ind = 0
        divided = False
        while divided == False:
            x = primes[ind]
            if val % x == 0:
                val /= x
                divided == True
            else:
                ind += 1
