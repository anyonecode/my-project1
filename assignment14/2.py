class division:
    li = 1
    # def __int__(self):
    #     pass
    def div(self,n):
        self.number = n
        for i in range(self.li,n):
            if i%7==0:
                yield i
    def show(self,l):
        p = division().div(l)
        for i in p:
            print(i)
a = division()
a.show(100)