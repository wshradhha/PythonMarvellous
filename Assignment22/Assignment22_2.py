import multiprocessing
import os

def FactorElement(myList):
    print(myList)
    sum = 0
    ProcessId = os.getpid()
    InputNo = myList
    for i in myList:
        
        fact = 1
        for j in range(1,i+1):
            fact = fact * j
        sum = sum + fact
    return ProcessId, InputNo, sum

 
def main():
    userList = []
    print("Enter how many number you want in list: ")
    value = int(input())
    print("Enter elements in list: ")
    for i in range(value):
        userList.append(int(input()))
    
    with multiprocessing.Pool() as pool:
        result = pool.map(FactorElement, [userList])
   
    print("Expected output: ")
        
    print(f"Process id, input number and Sum of factors of element is: {result[0]}")  


if __name__ == "__main__":
    main()
