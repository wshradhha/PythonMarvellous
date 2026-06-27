def getOdd(No1):
    for i in range(1,No1+1):
        if i % 2 != 0:
            print(i) 
        
def main():
    Value = int(input("Enter a number: "))
    getOdd(Value)

if __name__ == "__main__":
    main()