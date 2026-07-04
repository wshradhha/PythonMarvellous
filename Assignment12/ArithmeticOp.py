def Addition(Value1,Value2):
    Add = Value1 + Value2
    return Add

def Substraction(Value1,Value2):
    Sub = Value1 - Value2
    return Sub

def Multiplication(Value1,Value2):
    Mult = Value1 * Value2
    return Mult

def Division(Value1,Value2):
    Div = Value1 / Value2
    return Div
    
def main():
    print("Enter A First Number: ")
    No1 = int(input())

    print("Enter A Second Number: ")
    No2 = int(input())
    
    AdditionAns = Addition(No1,No2) 
    print("Addition is:- ",AdditionAns)

    SubstractionAns = Substraction(No1,No2) 
    print("Substraction is:- ",SubstractionAns)

    MultiplicationAns = Multiplication(No1,No2) 
    print("Multiplication is:- ",MultiplicationAns)

    DivisionAns = Division(No1,No2) 
    print("Division is:- ",DivisionAns)
    
if __name__ == "__main__":
    main()        
