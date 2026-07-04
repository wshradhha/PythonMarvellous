def PrintTillGivenNo(Value):
    for i in range(1,Value+1):
        print(i)
    
def main():
    print("Enter A Number: ")
    No = int(input())
    PrintTillGivenNo(No)

if __name__ == "__main__":
    main()        
