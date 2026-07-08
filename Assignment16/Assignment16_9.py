def printEven(No1):
    for i in range(2,((No1+1)*2),2):
        print(f"{i}  ", end="")
    

def main():
    Value1 = int(input("Enter a how many even no you want me to print on screen: ")) 

    printEven(Value1)

if __name__ == "__main__":
    main()