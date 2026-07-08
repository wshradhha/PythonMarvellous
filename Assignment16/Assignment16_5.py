def printNo(No1):
    for i in range(No1,0,-1):
        print(f" {i} ")
    
def main():
    Value1 = int(input("Enter a Number: ")) 

    Ret = printNo(Value1)

if __name__ == "__main__":
    main()