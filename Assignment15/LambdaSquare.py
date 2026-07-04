Square = lambda No : No * No

def main():
    Data = []
    print("how many No you want to enter: ")
    No = int(input())
    print("Enter No's: ")
    for i in range(No):
        Data.append(int(input()))
    print("Input Data is: ", Data)
    MData = list(map(Square, Data)) 
    print("Data after map: ", MData)

if __name__ == "__main__":
    main()  