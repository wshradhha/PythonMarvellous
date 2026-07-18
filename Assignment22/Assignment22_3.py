import multiprocessing

def primeElement(number):
    if(number < 2):
        return False
    for i in range(2,number):
        if(number%i==0):
            return False
    return True
  
def CntprimeElement(n):
    cnt = 0
    for i in range(1,n+1):
        if(primeElement(i)):
            cnt = cnt + 1
    return cnt
 
def main():
    userList = []
    print("Enter how many number you want in list: ")
    value = int(input())
    print("Enter elements in list: ")
    for i in range(value):
        userList.append(int(input()))
    
    with multiprocessing.Pool() as pool:
        result = pool.map(CntprimeElement, userList)
   
    for n,count in zip(userList,result):
        
        print(f"Total prime count between 1 and {n}: {count}")  


if __name__ == "__main__":
    main()