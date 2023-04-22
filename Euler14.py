longest = 0
val = 0
for i in range(1,1000000):
    sequence = [i]
    x = i
    while x != 1:
        if x % 2 == 0:
            x /= 2
        else:
            x = 3*x + 1
        sequence.append(x)
    if len(sequence) > longest:
        longest = len(sequence)
        val = i
    print(i)
print("longest: ", i)
print("length: ", longest)

