chkOdd = lambda Value1: Value1 % 2 != 0

def main():
    No1 = int(input("Enter 1st Number: "))

    oddNo = chkOdd(No1)
    if oddNo == True:
        print(No1,"is Odd no")
    else:    
        print(No1,"is not Odd no")

if __name__ == "__main__":
    main()
