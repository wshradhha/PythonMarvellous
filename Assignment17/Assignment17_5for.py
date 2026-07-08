def pattern(No1):
    for i in range(No1,1,-1):
        for j in range(i):
            print("*",end="\t")
        print()

def main():
    Value1 = int(input("Enter first number: "))

    pattern(Value1)

if __name__ == "__main__":
    main()