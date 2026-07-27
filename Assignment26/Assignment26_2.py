class Circle:
    PI=3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference1 = 0.0

    def Accept(self):
        print("Enter radius of the circle:")
        self.Radius = float(input())

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def Circumference(self):
        self.Circumference1= 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius: ",self.Radius)
        print("Area: ",self.Area)
        print("Circumference: ",self.Circumference1)
        print("-"*30)


print("---------Obj1------------")
obj1 = Circle()
obj1.Accept()
obj1.CalculateArea()
obj1.Circumference()
obj1.Display()

print("---------Obj2------------")
obj2 = Circle()
obj2.Accept()
obj2.CalculateArea()
obj2.Circumference()
obj2.Display()