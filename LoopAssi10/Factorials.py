def getFactorials(No1):
    Facto = 1
    for i in range(1,No1+1):
        Facto = Facto * i
    return Facto

        
def main():
    Value = int(input("Enter a number: "))
    Factorials = getFactorials(Value)
    print("Sum of natural no is: ",Factorials)

if __name__ == "__main__":
    main()