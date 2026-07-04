import math

def checkDigit(No):
    reversed = 0
    NO = abs(No)
    if(No==0):
        return 0
    while(No>0):
        remainder = No % 10
        reversed = (reversed*10)+remainder
        No = math.floor(No / 10)
        
    return reversed

def main():
    Value = int(input("Enter a number: "))
    Ret = checkDigit(Value)
    print("Reverse number is: ",Ret)

if __name__ == "__main__":
    main()