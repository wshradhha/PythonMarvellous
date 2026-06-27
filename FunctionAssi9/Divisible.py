def isDivisible(No1):
    if No1 % 3 == 0 and No1 % 5 == 0:
        return True
    else:
        return False

def main():
    Value1 = int(input("Enter a number: "))
    Divisible = isDivisible(Value1)
    if Divisible == True:
        print(Value1,"is Divisible of 3 and 5 ")
    else:
        print(Value1,"is not Divisible of 3 and 5")

if __name__ == "__main__":
    main()

