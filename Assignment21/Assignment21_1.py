import threading

def checkPrime(myList):
    listPrime = []
    
    for i in myList:
        is_prime = True
        if i < 2:
            continue
        for j in range(2,i):
            if(i % j == 0):
                is_prime = False
                break
        if is_prime == True:
            listPrime.append(i)
    print("Prime numbers are: ",listPrime)

def checkNonPrime(myList):
    listPrime1 = []
    
    for i in myList:
        is_Non_prime = False
        if i < 2:
            listPrime1.append(i)
            continue
        for j in range(2,i):
            if(i % j == 0):
                is_Non_prime = True
                break
        if is_Non_prime == True:
            listPrime1.append(i)
    print("Non Prime numbers are: ",listPrime1)
 
def main():
    userList = []
    print("Enter how many number you want in list: ")
    value = int(input())
    print("Enter elements in list: ")
    for i in range(value):
        userList.append(int(input()))
    Tobj1 = threading.Thread(target=checkPrime, args=(userList,))
    Tobj2 = threading.Thread(target=checkNonPrime, args=(userList,))

    Tobj1.start()
    Tobj2.start()
    Tobj1.join()
    Tobj2.join()


if __name__ == "__main__":
    main()
