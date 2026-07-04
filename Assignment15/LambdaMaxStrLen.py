from functools import reduce

MaxStrLen = lambda str1,str2: max(str1,str2, key=len)

def main():

    Data = []
    print("how many No you want to enter: ")
    No = int(input())
    print("Enter No's: ")
    for i in range(No):
        Data.append(input())
    print("Input Data is: ", Data)
    RData = reduce(MaxStrLen, Data)
    print("Data after Reduce and Max length string is: ", RData)

if __name__ == "__main__":
        main()
