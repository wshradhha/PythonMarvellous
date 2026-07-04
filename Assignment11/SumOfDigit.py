import math

def checkDigit(No):
    sum = 0
    NO = abs(No)
    if(No==0):
        return 0
    while(No>0):
        No1 = No % 10
        No = math.floor(No / 10)
        sum=sum + No1
    return sum

def main():
    Value = int(input("Enter a number: "))
    Ret = checkDigit(Value)
    print("Sum of Digit is: ",Ret)

if __name__ == "__main__":
    main()