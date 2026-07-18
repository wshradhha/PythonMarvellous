def AdditionOfElements(list1):
    sum = 0
    for i in range(len(list1)):
        sum = sum + list1[i]

    return sum

def main():
    No1 = int(input("Enter how many numbers you want to to add in list: "))
    print("Enter elements of list: ")
    MyList = []
    for i in range(No1):
        no=int(input())
        MyList.append(no)
    Add = AdditionOfElements(MyList)
    print(f"Addition of all element in list{MyList} is:",Add)

if __name__ == "__main__":
    main()