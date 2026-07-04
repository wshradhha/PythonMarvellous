from functools import reduce

Product = lambda No1, No2: No1 * No2

def main():
    Data = []
    print("how many No you want to enter: ")
    No = int(input())
    print("Enter No's: ")
    for i in range(No):
        Data.append(int(input()))
    print("Input Data is: ", Data)
    RData = reduce(Product, Data)
    print("Product of all elements: ", RData)

if __name__ == "__main__":
        main()
