day = month = year = 1
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while year <= 100:
    while month <= 12:
        if month != 2:
            if year % 4 == 0 and year % 400 != 0:
                days = 29
            else:
                days = 28
        else:
            days = months[month - 1]
        
        month += 1
