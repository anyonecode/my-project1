x = int(input('enter first number'))
y = int(input('enter second number'))
z = int(input('enter third number'))
if (x>y)&(x>z):
    if (y>z):
        print('second number is the second largest number')
    else:
        print('third number is the second largest number')
if(y>x)&(y>z):
    if (x>z):
        print('first number is the second largest number')
    else:
        print('third number is the second largest number')
if (z>x)&(z>y):
    if (x>y):
        print('first number is the second largest number')
    else:
        print('second number is the second largest number')