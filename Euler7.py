i = 0
j = 0
factors = 0
total = 1
while total < 10001:
    i += 1
    factors = 0
    if i%2 == 1:
        for j in range(1,int((i+1)/2)):
            if i%j == 0:
                factors += 1
    if factors == 1:
        total += 1
        print(i)
