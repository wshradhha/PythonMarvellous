import math

def SumDigit(No1):
    sum = 0
    while(No1):
        digit = No1 % 10
        sum = sum + digit
        No1 = math.floor(No1 / 10)
    return sum
       
def main():
    Value1 = int(input("Enter number: "))

    Calcultion = SumDigit(Value1)

    print(f"Sum of digits of {Value1} is: {Calcultion}")

if __name__ == "__main__":
    main()