t, p, h = [], [], []
n = 0
while True:
    n += 1
    h.append(n*(2*n-1))
    p.append(n*(3*n-1)/2)
    x = n*(n+1)/2
    print(x)
    if x in h and x in p and x != 1 and x != 40755:
        break

