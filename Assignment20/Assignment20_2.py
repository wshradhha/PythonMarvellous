import threading
import time

def PrintSumEvenFactor(No):
    sum = 0
    for i in range(1,No+1):
        if(No % i == 0 and i % 2 == 0):
            sum = sum + i
    print("Sum of even factor is: ",sum)

def PrintSumOddFactor(No):
    sum = 0
    for i in range(1,No+1):
        if(No % i == 0 and i % 2 != 0):
            sum = sum + i
    print("Sum of odd factor is: ",sum)

def main():
    start_time = time.perf_counter()

    print("Enter Number to get Sum of Even factors:")
    No1 = int(input())

    print("Enter Number to get Sum of Odd factors:")
    No2 = int(input())

    tobj1= threading.Thread(target=PrintSumEvenFactor, args=(No1,))
    tobj2= threading.Thread(target=PrintSumOddFactor, args=(No2,))

    tobj1.start()
    tobj2.start()
    
    tobj1.join()
    tobj2.join()
    
    end_time = time.perf_counter()

    print(f"Time required is :{end_time - start_time : .5f} ")

if __name__ == "__main__":
    main()




