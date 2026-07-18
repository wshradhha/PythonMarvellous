import multiprocessing
import time

def PowerElement(number):
    sum = 0
    for i in range(1,number+1):
        sum = sum + i**5      #**used to take power
    return sum  
 
def main():
    userList = []
    print("Enter how many number you want in list: ")
    value = int(input())
    print("Enter elements in list: ")
    for i in range(value):
        userList.append(int(input()))

    start_time = time.perf_counter()
    
    with multiprocessing.Pool() as pool:
        result = pool.map(PowerElement, userList)

    end_time = time.perf_counter()
    for n,sum in zip(userList,result):
        print(f"Total sum of {n}: {sum}")  

    total_time = end_time-start_time
    print(f"Total execution time: {total_time:.4f} Seconds")


if __name__ == "__main__":
    main()