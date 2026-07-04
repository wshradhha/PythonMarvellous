import math

def checkDigit(No):
    reversed = 0
    NO = abs(No)
    OrigionalNo = No
    if(No>0 and No<10):
        print("inside if")
        return True
    while(No>0):
        remainder = No % 10
        reversed = (reversed*10)+remainder
        No = math.floor(No / 10)
        
    if (reversed == OrigionalNo):
        print(reversed == OrigionalNo)
        return True
    else:
        return False

def main():
    Value = int(input("Enter a number: "))
    Ret = checkDigit(Value)
    if(Ret == True):
        print(Value,"number is Palindrome: ",Value)
    else:
        print(Value,"number is Not Palindrome: ",Value)

if __name__ == "__main__":
    main()