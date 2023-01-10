class person:
    def __init__(self,name,place):
        self.name = name
        self.place = place
    def add(self):
        print('my name is ',self.name,"my place is ",self.place)
A = person("sreehari","tirur")
A.add()

class person:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        print(self.a+self.b)
A = person(12,13)
A.add()

class A:
    i = 1234
    def __init__(self):
        self.i=123456
print(A.i)
print(A().i)
