Mult = lambda Value1, Value2: Value1 * Value2

def main():
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter Two number: "))
    Multiplication = Mult(No1,No2)

    print("Multiplication of",No1,"and",No2,"is: ",Multiplication)

if __name__ =="__main__":
    main()