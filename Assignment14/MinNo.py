min = lambda Value1, Value2: Value1 < Value2

def main():
    No1 = int(input("Enter 1st Number: "))
    No2 = int(input("Enter 2nd Number: "))
    maxNo = min(No1,No2)
    if maxNo == True:
        print(No1,"is Min no")
    else:    
        print(No2,"is Min no")

if __name__ == "__main__":
    main()
