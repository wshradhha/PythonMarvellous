import threading
import time

def EvenList(MyList):
    Sum = 0
    for i in range(MyList):
        if(i % 2 == 0):
            Sum = Sum + i
    print("Sum of Even no's is:",Sum)

def OddList(MyList):
    Sum = 0
    for i in range(MyList):
        if(i % 2 != 0):
            Sum = Sum + i
    print("Sum of Odd no's is:",Sum)

def main():
    start_time = time.perf_counter()
    print("Enter length of List")
    No1 = int(input())

    List = []
    print("Enter elements of List")
    for i in range(No1):
        List.append(i)
    
    tobj1 = threading.Thread(target=EvenList, args=(List,))
    
    tobj2 = threading.Thread(target=OddList, args=(List,))

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()
    end_time = time.perf_counter()
    print(f"Time required is :{end_time - start_time : .5f} ")

if __name__ == "__main__":
    main()




