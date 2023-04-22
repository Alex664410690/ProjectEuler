def PrimeSums(x, t, c, n):
    p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i in p[n:]:
        if x + i < t:
            c += PrimeSums(x + i, t, c, i + n - 1)
        elif x + i == t:
            return 1
        else:
            break
    return c

print(PrimeSums(0, 71, 0, 0))
