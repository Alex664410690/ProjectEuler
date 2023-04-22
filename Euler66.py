def getNums():
    squares = [x*x for x in range(32)]
    lst = []
    for i in range(1, 1001):
        if i not in squares:
            lst.append(i)
    return lst

def dioPhantine():
    largest = 0
    value = 0
    for i in getNums():
        x = 1
        found = False
        while not found:
            for y in range(1, x):
                if x*x - i*y*y == 1:
                    print(f"{x}^2 - {i}*{y}^2")
                    if x > largest:
                        largest = x
                        value = i
                    found = True
                    break
            x += 1
    print(largest)


dioPhantine()