import multiprocessing
import os

def EvenElement(number):
    processId = os.getpid()
    sum = 0
    for i in range(1,number+1):
        if(i%2==0):
            sum = sum + i
    return processId,sum  
 
def main():
    userList = []
    print("Enter how many number you want in list: ")
    value = int(input())

    print("Enter elements in list: ")
    
    for i in range(value):
        userList.append(int(input()))
    
    with multiprocessing.Pool() as pool:
        result = pool.map(EvenElement, userList)

    for n,sumEven in zip(userList,result):
        print(f"Process ID: {sumEven[0]}")
        print(f"Input Number: {n}")
        print(f"Total sum of even no {n}: {sumEven[1]}")  

if __name__ == "__main__":
    main()