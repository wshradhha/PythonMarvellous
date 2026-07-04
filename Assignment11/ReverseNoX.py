import math

def ReverseNo(No):
    reversed = 0
    if(No==0):
        return 0
    else:
        reversed = No[::-1]
        
    return reversed

def main():
    Value = (input("Enter a number: "))
    Ret = ReverseNo(Value)
    print("Reverse number is: ",Ret)

if __name__ == "__main__":
    main()