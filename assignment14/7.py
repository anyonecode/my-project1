class rectangle :
    def __init__(self,b,h):
        self.b = b
        self.h = h
    def area(self):
        print('area :',self.b*self.h)
a = rectangle(5,6)
a.area()