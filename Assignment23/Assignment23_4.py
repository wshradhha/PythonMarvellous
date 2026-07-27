import multiprocessing
import os

def CntOddElement(number):
    processId = os.getpid()
    cnt = 0
    for i in range(1,number+1):
        if(i%2!=0):
            cnt = cnt + 1
    return processId,cnt  
 
def main():
    userList = []
    print("Enter how many number you want in list: ")
    value = int(input())

    print("Enter elements in list: ")
    
    for i in range(value):
        userList.append(int(input()))
    
    with multiprocessing.Pool() as pool:
        result = pool.map(CntOddElement, userList)

    for n,cntOdd in zip(userList,result):
        print(f"Process ID: {cntOdd[0]}")
        print(f"Input Number: {n}")
        print(f"Total count of even no {n}: {cntOdd[1]}")  

if __name__ == "__main__":
    main()