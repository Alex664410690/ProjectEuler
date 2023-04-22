import math
cubes = []
for i in range(10000):
    z = [x for x in str(i*i*i)]
    z.sort()
    z = (i, z)
    cubes.append(z)

for i in cubes:
    count = []
    print(i[0])
    for j in cubes:
        if i[1] == j[1]:
            count.append(j)
    if len(count) == 5:
        break
    
