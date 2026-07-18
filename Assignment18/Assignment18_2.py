def MaxOfElements(list1):
    max = 0
    for i in range(len(list1)):
        if(list1[i]>max):
            max = list1[i]
    return max

def main():
    No1 = int(input("Enter how many numbers you want to to add in list: "))
    print("Enter elements of list: ")
    MyList = []
    for i in range(No1):
        no=int(input())
        MyList.append(no)
    Max = MaxOfElements(MyList)
    print(f"Addition of all element in list{MyList} is:",Max)

if __name__ == "__main__":
    main()