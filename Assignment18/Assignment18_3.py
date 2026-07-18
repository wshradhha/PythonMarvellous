def MinOfElements(list1):
    mini = list1[0]
    for i in range(len(list1)):
        
        if(list1[i]<mini):
            print(list1[i])
            mini = list1[i]
    return mini

def main():
    No1 = int(input("Enter how many numbers you want to to add in list: "))
    print("Enter elements of list: ")
    MyList = []
    for i in range(No1):
        no=int(input())
        MyList.append(no)
    Min = MinOfElements(MyList)
    print(f"Addition of all element in list{MyList} is:",Min)

if __name__ == "__main__":
    main()