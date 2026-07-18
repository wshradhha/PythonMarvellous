import MarvellousNum

def main():
    No1 = int(input("Enter how many numbers you want to to add in list: "))
    print("Enter elements of list: ")
    MyList = []
    for i in range(No1):
        no=int(input())
        MyList.append(no)
    Add = MarvellousNum.AdditionOfElements(MyList)
    print(f"Addition of all element in list{MyList} is:",Add)

if __name__ == "__main__":
    main()