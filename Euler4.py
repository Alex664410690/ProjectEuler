num = 0
intNum = 0
largest = 0
for i in range(1,1000):
    for j in range(1,1000):
        num = i * j
        print(i)
        num = [int(x) for x in str(num)]
        if num == num[::-1]:
            num = [str(x) for x in num]
            numString = "".join(num)
            intNum = int(numString)
            if intNum > largest:
                largest = intNum
print(largest)