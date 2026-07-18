def SearchElements(list1, No):
    
    cnt = 0
    for i in range(len(list1)):
        if(list1[i]==No):
            cnt = cnt + 1
    return cnt

def main():
    No1 = int(input("Enter how many numbers you want to to add in list: "))
    print("Enter elements of list: ")
    MyList = []
    for i in range(No1):
        no=int(input())
        MyList.append(no)
    No2 = int(input("Number to search: "))
    Freq = SearchElements(MyList, No2)
    if(Freq == 0):
        print("No not available in list.")
    else:
        print(f"{No2} : find in list{MyList} : {Freq} times")

if __name__ == "__main__":
    main()