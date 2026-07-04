import math

def checkDigit(No):
    cnt = 0
    NO = abs(No)
    if(No==0):
        return 0
    while(No>0):
        No = math.floor(No / 10)
        cnt=cnt+1

    return cnt

def main():
    Value = int(input("Enter a number: "))
    Ret = checkDigit(Value)
    print("Count of number is: ", cnt)

if __name__ == "__main__":
    main()