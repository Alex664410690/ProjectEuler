import math
def perms(nums, value):
    if len(nums) == 0:
        return [value]
    finals = []
    for i in nums:
        temp = nums.copy()
        temp.remove(i)
        finals += perms(temp, value+str(i))
    return finals
def prime(x):
    for i in range(2, round(math.sqrt(x))):
        if x % i == 0:
            return False
    return True
largest = 0
for i in range(2, 5):
    ints = [x for x in range(1, i+1)]
    for j in perms(ints, ""):
        print(j)
        if prime(int(j)) and int(j) > largest:
            largest = int(j)
print(largest)