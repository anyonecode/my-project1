# tax
cost = int(input('enter the cost of the product'))
if cost < 1000 & cost > 0:
    tax = ((cost*5)/100)
    amt = tax+cost
    print("the cost of tbe product with tax" , amt)
elif cost >1000 & cost<25000:
    tax = ((cost * 10) / 100)
    amt = tax + cost
    print("tax is " , tax)
    print("the cost of tbe product with tax", amt)
elif cost > 25000:
    tax = ((cost * 20) / 100)
    amt = tax + cost
    print("tax is " , tax)
    print("the cost of tbe product with tax", amt)
else:
    print('there is no cost for your product')
