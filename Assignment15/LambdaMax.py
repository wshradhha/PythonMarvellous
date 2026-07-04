from functools import reduce

Maximum = lambda No1, No2: max(No1, No2)

def main():
    Data = []
    print("how many No you want to enter: ")
    No = int(input())
    print("Enter No's: ")
    for i in range(No):
        Data.append(int(input()))
    print("Input Data is: ", Data)
    RData = reduce(Maximum, Data)
    print("Data after reduce: ", RData)

if __name__ == "__main__":
        main()
