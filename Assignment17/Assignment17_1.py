import Arithmatic as Math
    
def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter first number: "))

    Add = Math.Addition(Value1, Value2)
    print(f"Addition of {Value1} and {Value2} is {Add}")
    Sub = Math.Substraction(Value1, Value2)
    print(f"Substraction of {Value1} and {Value2} is {Sub}")
    Mult = Math.Multiplication(Value1, Value2)
    print(f"Multiplication of {Value1} and {Value2} is {Mult}")
    Div = Math.Division(Value1, Value2)
    print(f"Division of {Value1} and {Value2} is {Div}")

if __name__ == "__main__":
    main()