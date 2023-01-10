class bus:
    def __init__(self,name,seat):
        self.name = name
        self.seat = seat
    def ammount(self):
        fare = self.seat*100
        amount_1 = fare+((10*fare)/100)
        print("total amount",amount_1)
A = bus("xxx",50)
A.ammount()

