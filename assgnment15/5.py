class str:
    a = [2,3,4,6,7]
class mystring(str):
    def append(self,b):
        self.a.append(b)
        print("the append list is :",self.a)
    def pop(self,c):
        self.a.pop(c)
        print("the pop list is :", self.a)
s = mystring()
s.append(10)
s.pop(3)