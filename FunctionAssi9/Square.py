def getSquare(No1):
    square = No1 * No1
    return square

def main():
    Value1 = int(input("Enter a number: "))
    sqr = getSquare(Value1)
    print("Square of ",Value1,"is : ",sqr)

if __name__ == "__main__":
    main()

