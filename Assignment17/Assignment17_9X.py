import math

def CalDigit(No1):
    Digits = len(str(No1))
    return Digits

def main():
    Value1 = int(input("Enter first number: "))

    digits=CalDigit(Value1)
    print(f"Digits in {Value1} is {digits}")

if __name__ == "__main__":
    main()