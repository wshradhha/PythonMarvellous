import math

def CalDigit(No1):
    cnt =0
    while(No1 % 10 !=0):
       
        digit = No1 % 10
        if(digit):
            cnt = cnt + 1
        No1 = math.floor(No1 / 10)
    return cnt

def main():
    Value1 = int(input("Enter first number: "))

    digits=CalDigit(Value1)
    print(f"Digits in {Value1} is {digits}")

if __name__ == "__main__":
    main()