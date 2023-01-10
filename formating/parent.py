class a :
    def em(self):
        print("am manager")
class b:
    def em1(self):
        print("am assistent")
class c(a,b):
    def em2(self):
        print("am worker")

obj = c()
obj.em1()