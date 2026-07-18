import threading

def checkMax(myList):
    max = 0
    for i in myList:
        if(i> max):
            max = i
    print("Max numbers is: ",max)

def checkMin(myList):
    mini = myList[0]
    for num in myList:
        if num < mini:
            mini = num
            
    print("Minimum number is:", mini)
 
def main():
    userList = []
    print("Enter how many number you want in list: ")
    value = int(input())
    print("Enter elements in list: ")
    for i in range(value):
        userList.append(int(input()))
    Tobj1 = threading.Thread(target=checkMax, args=(userList,))
    Tobj2 = threading.Thread(target=checkMin, args=(userList,))

    Tobj1.start()
    Tobj2.start()
    Tobj1.join()
    Tobj2.join()


if __name__ == "__main__":
    main()
