def MultTable(No1):
    endstp = No1 * 11
    for i in range(No1,endstp,No1):
        print(i)

def main():
    Value = int(input("Enter a number: "))
    MultTable(Value)

if __name__ == "__main__":
    main()