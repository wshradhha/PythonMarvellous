def chkGreater(no1, no2):
    if no1 > no2:
        return no1
    else:
        return no2
    
def main():
    Value1=int(input("Enter First number:- "))
    Value2=int(input("Enter second number:- "))

    GreaterNo = chkGreater(Value1,Value2)
    print("Greater from",Value1,"and",Value2,"is:- ", GreaterNo)

if __name__ == "__main__":
    main()