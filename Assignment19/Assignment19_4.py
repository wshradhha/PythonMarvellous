from functools import reduce 

def CheckEvenNum(value):
    return(value % 2 ==0)

def SquareNum(value):
    return value*value

def AddNum(x,y):
    return x+y

def main():
    No1 = int(input("Enter how many numbers you want in list: "))
    
    List = []

    print("Enter elements for list: ")
    for i in range(No1):
        List.append(int(input()))

    fData = list(filter(CheckEvenNum,List))
    print(f"{List} Data filtered is:",fData)

    mData = list(map(SquareNum,fData))
    print(f"{fData} Data mapped is:",mData)

    rData = reduce(AddNum,mData)
    print(f"{mData} Data's product is:",rData)

if __name__ == "__main__":
    main()