import random
Squares = ['GO', 'A1', 'CC', 'A2', 'T1', 'R1', 'B1', 'CH', 'B2', 'B3', 'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC', 'D2', 'D3', 'FP', 'E1', 'CH', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 'G2J', 'G1', 'G2', 'CC', 'G3', 'R4', 'CH', 'H1', 'T2', 'H2']
landed = [0 for x in range(40)]
Chance = [x for x in range(1, 17)]
random.shuffle(Chance)
ComChest = [x for x in range(1, 17)]
random.shuffle(ComChest)
location = 0
for i in range(1000000):
    doubles = 0
    rolling = True
    while rolling == True:
        rolling = False
        d1 = random.randint(1, 4)
        d2 = random.randint(1, 4)
        location += d1 + d2
        if location > 39:
            location -= 40
        if d1 == d2:
            doubles += 1
            rolling = True
        if doubles == 3:
            location = 10
        if Squares[location] == 'CC':
            c = ComChest.pop(0)
            ComChest.append(c)
            if c == 1:
                location = 0
            elif c == 2:
                location = 10
        elif Squares[location] == 'CH':
            c = Chance.pop(0)
            Chance.append(c)
            if c == 1:
                location = 0
            elif c == 2:
                location = 10
            elif c == 3:
                location = 11
            elif c == 4:
                location = 24
            elif c == 5:
                location = 39
            elif c == 6:
                location = 5
            elif c == 7 or c == 8:
                if location < 5 or location > 35:
                    location = 5
                elif location < 15:
                    location = 15
                elif location < 25:
                    location = 25
                elif location < 35:
                    location = 35
            elif c == 9:
                if location < 12 or location > 28:
                    location = 12
                elif location < 28:
                    location = 28
            elif c == 10:
                location -= 3
        if location == 30:
            location = 10
        landed[location] += 1
totals = [(Squares[i], landed[i], i) for i in range(40)]
totals.sort(key=lambda tup: tup[1])
totals.reverse()
for i in totals:
    print(i)
string = ""
for i in totals[:3]:
    if len(str(i[2])) == 1:
        string += "0"
        string += str(i[2])
    else:
        string += str(i[2])
print(string)