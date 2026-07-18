import threading

def PrintNumber(No1):
    for i in range(1,No1+1):
        print(i,end="\t")

def PrintNumberRev(No1):
    print()
    for i in range(No1,0,-1):
        print(i,end="\t")

def main():
    print("Enter a number till you want to display numbers: ")
    Value = int(input())

    Tobj1 = threading.Thread(target=PrintNumber, args=(Value,))
    Tobj2 = threading.Thread(target=PrintNumberRev, args=(Value,))

    Tobj1.start()
    Tobj1.join()
    Tobj2.start()
    Tobj2.join()


if __name__ == "__main__":
    main()