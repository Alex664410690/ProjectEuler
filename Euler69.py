def PrimeFactors(x):
    factors = []
    while x > 1:
        for i in range(2, x+1):
            if x % i == 0:
                factors.append(i)
                x = int(x / i)
                break
    return factors

def RelativePrime(x):
    count = 0
    for i in range(1, x):
        found = False
        for j in PrimeFactors(x):
            if j in PrimeFactors(i):
                found = True
                break
        if found == False:
            count += 1
    return count

largest = 0
largestN = 0
for i in range(510500, 510520):
    print(i)
    ratio = i / RelativePrime(i)
    if ratio > largest:
        largest = ratio
        largestN = i
print(largestN)