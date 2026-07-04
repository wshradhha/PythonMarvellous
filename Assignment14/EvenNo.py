chkEven = lambda Value1: Value1 % 2 == 0

def main():
    No1 = int(input("Enter 1st Number: "))

    evenNo = chkEven(No1)
    if evenNo == True:
        print(No1,"is Even no")
    else:    
        print(No1,"is not Even no")

if __name__ == "__main__":
    main()
