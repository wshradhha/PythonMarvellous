def getCube(No1):
    Cube = No1 * No1 * No1
    return Cube

def main():
    Value1 = int(input("Enter a number: "))
    Cube1 = getCube(Value1)
    print("Cube of ",Value1,"is : ",Cube1)

if __name__ == "__main__":
    main()

