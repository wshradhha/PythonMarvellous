def PrintTillGivenNoRev(Value):
    for i in range(Value,0,-1):
        print(i)
    
def main():
    print("Enter A Number: ")
    No = int(input())
    PrintTillGivenNoRev(No)

if __name__ == "__main__":
    main()        
