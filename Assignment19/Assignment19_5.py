from functools import reduce 

def CheckPrimeNum(value):
    is_prime = True
    if(value % 2==0):
        is_prime = False
    else:
        return value

def MultNum(value):
    return value*2

def addNum(x,y):
    return x + y

def main():
    No1 = int(input("Enter how many numbers you want in list: "))
    
    List = []

    print("Enter elements for list: ")
    for i in range(No1):
        List.append(int(input()))

    fData = list(filter(CheckPrimeNum,List))
    print(f"{List} Data filtered is:",fData)

    mData = list(map(MultNum,fData))
    print(f"{fData} Data mapped is:",mData)

    rData = reduce(addNum,mData)
    print(f"{mData} Data's product is:",rData)

if __name__ == "__main__":
    main()