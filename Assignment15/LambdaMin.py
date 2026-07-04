from functools import reduce

Minimum = lambda No1, No2: min(No1, No2)

def main():
    Data = []
    print("how many No you want to enter: ")
    No = int(input())
    print("Enter No's: ")
    for i in range(No):
        Data.append(int(input()))
    print("Input Data is: ", Data)
    RData = reduce(Minimum, Data)
    print("Data after reduce and mininum no is: ", RData)

if __name__ == "__main__":
        main()
