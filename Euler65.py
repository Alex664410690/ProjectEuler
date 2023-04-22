import fractions
def F(con):
    f = []
    for i in range(1, con // 3 + 2):
        f.append(1)
        f.append(2*i)
        f.append(1)
    return f

def E(con, pos):
    if pos == con:
        return F(con)[pos]
    return fractions.Fraction(numerator=1, denominator=F(con)[pos]+E(con, pos+1))

print(sum([int(x) for x in str(fractions.Fraction(E(100, 0) + 2).numerator)]))