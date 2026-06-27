def getSumNatNo(No1):
    total = 0
    for i in range(1,No1+1):
        total = total + i
    return total

        
def main():
    Value = int(input("Enter a number: "))
    SumOfNaturalNo = getSumNatNo(Value)
    print("Sum of natural no is: ",SumOfNaturalNo)

if __name__ == "__main__":
    main()