def MultTable(No1):
    for i in range(1,11):
        print(No1*i)

def main():
    Value = int(input("Enter a number: "))
    MultTable(Value)

if __name__ == "__main__":
    main()