from functools import reduce 

def CheckNum(value):
    dataList = []
    if(value >= 70 and value <= 90):
        dataList.append(value)
    return dataList

def IncreaseNum(value):
    return value+10

def MultNum(x,y):
    return x*y
        


def main():
    No1 = int(input("Enter how many numbers you want in list: "))
    List = []
    print("Enter elements for list: ")
    for i in range(No1):
        List.append(int(input()))
    fData = list(filter(CheckNum,List))
    print(f"{List} Data filtered is:",fData)
    mData = list(map(IncreaseNum,fData))
    print(f"{fData} Data mapped is:",mData)
    rData = reduce(MultNum,mData)
    print(f"{mData} Data's product is:",rData)

if __name__ == "__main__":
    main()