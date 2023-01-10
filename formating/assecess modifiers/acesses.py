class person:
    def __init__(self,name,place):
        self._name = name
        self._place = place
    def add(self):
        print('my name is ',self._name,"my place is ",self._place)
A = person("sreehari","tirur")
A.add()

class person:
    def __init__(self,a,b):
        self._a = a
        self._b = b
    def add(self):
        print(self._a+self._b)
A = person(12,13)
A.add()
