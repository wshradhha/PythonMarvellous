import threading
import time

def PrintEven(No):
    EvenList = []
    for i in range(No):
        if(i % 2 == 0):
            EvenList.append(i)
    print("First 10 even no's are",EvenList)

def PrintOdd(No):
    OddList = []
    for i in range(No):
        if(i % 2 != 0):
            OddList.append(i)
    print("First 10 Odd no's are",OddList)

def main():
    start_time = time.perf_counter()

    tobj1= threading.Thread(target=PrintEven, args=(21,))
    tobj2= threading.Thread(target=PrintOdd, args=(21,))

    tobj1.start()
    tobj2.start()
    
    tobj1.join()
    tobj2.join()
    
    end_time = time.perf_counter()

    print(f"Time required is :{end_time - start_time : .5f} ")

if __name__ == "__main__":
    main()




