def factors(n):
    total = 0
    for i in range(n//2+1):
        if n % 1 == 0:
            total += i
    return total
sum = 0
for i in range(10000):
    print(i)
    if i == factors(factors(i)):
        sum += i
print(sum)
