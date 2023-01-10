class new:
    def __int__(self):
        self.str = " "
    def getstring(self):
        self.str = input("enter a string")
    def printstring(self):
        print(self.str.upper())

a = new()
a.getstring()
a.printstring()