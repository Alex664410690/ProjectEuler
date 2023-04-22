def palindrome(num):
    counter = 0
    while str(num) != str(num)[::-1] and counter <= 50:
        num += int(str(num)[::-1])
        counter += 1
    return counter
lychrel = 0
for i in range(10000):
    print(palindrome(i))
    if palindrome(i) >= 50:
        lychrel += 1
print(lychrel)
