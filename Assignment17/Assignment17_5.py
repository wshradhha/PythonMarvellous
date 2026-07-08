def pattern(No1):
    while(No1 !=0):
        print("*\t"*No1)
        No1 = No1 - 1

def main():
    Value1 = int(input("Enter first number: "))

    pattern(Value1)

if __name__ == "__main__":
    main()