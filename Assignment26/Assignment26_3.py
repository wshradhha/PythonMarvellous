class Arithmatic:

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        self.value1 = int(input("Enter first number"))
        self.value2 = int(input("Enter second number"))

    def Addition(self):
        Addition = self.value1 + self.value2
        print(f"Addition of {self.value1} and {self.value2} is: ",Addition)

    def Substraction(self):
        Sub = self.value1 - self.value2
        print(f"Substraction of {self.value1} and {self.value2} is: ",Sub)

    def Multiplication(self):
        Mult = self.value1 * self.value2
        print(f"Multiplication of {self.value1} and {self.value2} is: ",Mult)

    def Division(self):
        if self.value2 == 0:
            print("Do not enter zero")
        else:
        
            Div = self.value1 / self.value2
            print(f"Division of {self.value1} and {self.value2} is: {Div}")

Aobj1 = Arithmatic()
Aobj1.Accept()
Aobj1.Addition()
Aobj1.Substraction()
Aobj1.Multiplication()
Aobj1.Division()

Aobj2 = Arithmatic()
Aobj2.Accept()
Aobj2.Addition()
Aobj2.Substraction()
Aobj2.Multiplication()
Aobj2.Division()

    

    