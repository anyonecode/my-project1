class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r

    def perimeter(self):
        return 2 * 3.14 * self.r

    def area(self):
        return 3.14 * self.r ** 2


    def point(self, x, y):
        return (x - self.a) ** 2 + (y - self.b) ** 2 - self.r ** 2


    def test_belong(self, x, y):
        if (self.point(x, y) == 0):
            print("the point: (", x, y, ") belongs to the circle C")
        else:
            print("the point: (", x, y, ") does not belong to the circle C")



C = Circle(1, 2, 1)

print("the perimeter of the circle C is:", C.perimeter())
print("the area of circle C is:", C.area())

C.test_belong(1, 2)