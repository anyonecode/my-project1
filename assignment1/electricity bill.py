#electricity bill
unt = int(input('enter the unit of electricity you use '))
if unt <100:
    amt = 0
    print('the amount you want to pay is' ,amt)
elif unt>100 & unt<200:
    amt = ((unt*5)/100)+unt
    print('the amount you want to pay is', amt)
elif unt>200:
    amt = ((unt*10)/100)+unt
    print('the amount you want to pay is', amt)
else:
    print('there is no electricity you use')
