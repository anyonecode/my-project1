k = int(input('enter  the day of the month'))
m = int(input('enter  the month number the month start from march'))
d = int(input('enter  the last two digits of the year'))
c = int(input('enter  the first two digits of the year'))
f = k+ ((13*m-1)/5) +d+ (d/4) +(c/4)-2*c
day = int(f % 7)
if day == 0:
    print('the day is sunday')
elif day == 1:
    print('the day is monday')
elif day == 2:
    print('the day is tuesday')
elif day == 3:
    print('the day is wednesday')
elif day == 4:
    print('the day is thursday')
elif day == 5:
    print('the day is friday')
elif day == 6:
    print('the day is saturday')
else:
    print('invalide input')
if m == 1:
    print(k,'march',c,d)
elif m == 2:
    print(k,'april',c,d)
elif m == 3:
    print(k,'may',c,d)
elif m == 4:
    print(k,'june',c,d)
elif m == 5:
    print(k,'july',c,d)
elif m == 6:
    print(k,'august',c,d)
elif m == 7:
    print(k,'september',c,d)
elif m == 8:
    print(k,'october',c,d)
elif m == 9:
    print(k,'november',c,d)
elif m == 10:
    print(k,'december',c,d)
elif m == 11:
    print(k,'january',c,d)
elif m == 12:
    print(k,'february',c,d)
else:
    print('invaild input')

