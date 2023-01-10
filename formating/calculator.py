n = int(input('enter a number'))
d = int(input('enter a number'))
k = str(input("enter the operation add/sub/mul/div"))
class a :
    def add(self):
        print(n+d)
class b:
    def sub(self):
        print(n-d)
class c:
    def mul(self):
        print(n*d)
class e:
    def div(self):
        print(n/d)

obj = e()
obj.k()