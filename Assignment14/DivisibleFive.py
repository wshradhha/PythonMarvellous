chkDivisible= lambda Value1: Value1 % 5 == 0

def main():
    No1 = int(input("Enter 1st Number: "))

    evenNo = chkDivisible(No1)
    if evenNo == True:
        print(No1,"is Divisible by 5")
    else:    
        print(No1,"is not Divisible by 5")

if __name__ == "__main__":
    main()
