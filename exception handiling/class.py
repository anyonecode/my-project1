class bus:
    def __init__(self,name,seat):
        self.name = name
        self.seat = seat
    def ammount(self):
        fare = self.seat*100
        amount_1 = fare+((10*fare)/100)
        print("total amount",amount_1)
try:
    name = input('enter a name')
    seat = int(input('enter seat'))
    A = bus(name,seat)
    A.ammount()
except ValueError:
    print('invalid value')


