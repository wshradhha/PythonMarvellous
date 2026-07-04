Odd = lambda No : No % 2 != 0

def main():
    Data = []
    print("how many No you want to enter: ")
    No = int(input())
    print("Enter No's: ")
    for i in range(No):
        Data.append(int(input()))
    print("Input Data is: ", Data)
    FData = list(filter(Odd, Data)) 
    print("Data after filter: ", FData)

if __name__ == "__main__":
        main()
