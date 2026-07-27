import multiprocessing
import os

def CntFactorsElement(number):
    processId = os.getpid()
    factor = 1
    for i in range(1,number+1):
        factor = factor * i
    return processId,factor  
 
def main():
    userList = []
    print("Enter how many number you want in list: ")
    value = int(input())

    print("Enter elements in list: ")
    
    for i in range(value):
        userList.append(int(input()))
    
    with multiprocessing.Pool() as pool:
        result = pool.map(CntFactorsElement, userList)

    for n,cntFact in zip(userList,result):
        print(f"Process ID: {cntFact[0]}")
        print(f"Input Number: {n}")
        print(f"Total count of even no {n}: {cntFact[1]}")  

if __name__ == "__main__":
    main()