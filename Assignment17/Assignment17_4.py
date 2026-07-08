
def PrimeNum(No):
    for i in range(2,No):
        if(No % i == 0):
            return False
    return True
       
def main():
    Value1 = int(input("Enter number: "))

    Fact = PrimeNum(Value1)
    if(Fact == True):
        print(f"{Value1} is Prime Number")
    else:
        print(f"{Value1} is not Prime Number")

if __name__ == "__main__":
    main()