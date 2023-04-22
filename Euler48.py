total = 0
for i in range(1, 1001):
    value = 1
    for j in range(i):
        value *= i
    total += value
print("Total:", str(total)[-10:])

