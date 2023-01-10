#area
no_side= int(input('enter the number of side'))
def square():
    x = float(input('enter the leghth'))
    area = (x*x)
    print('area is ',area)
def triangle():
    x = float(input('enter the leghth'))
    y = float(input('enter the height'))
    area = (x * y)/2
    print('area is ',area)
def circle():
    r = float(input('enter the radius'))
    pi=3.14
    area = (pi*(r*r))
    print('area is ', area)
def pentgon():
    x = float(input('enter the perimeter'))
    y = float(input('enter the apothem'))
    area = ((5*x) * y)/2
    print('area is ', area)
if (no_side == 4):
    print('it is a square')
    square()
elif (no_side == 3):
    print('it is a triagle')
    triangle()
elif (no_side == 0):
    print('it is a circle')
    circle()
elif(no_side == 5):
    print('it is a pentgon')
    pentgon()
else:
    print('it is a in valid input')