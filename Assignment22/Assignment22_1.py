import multiprocessing

def SumElement(myList):
    sum = 0
    for i in myList:
        square = i*i
        sum = sum + square
    return sum

 
def main():
    userList = []
    print("Enter how many number you want in list: ")
    value = int(input())
    print("Enter elements in list: ")
    for i in range(value):
        userList.append(int(input()))
    
    with multiprocessing.Pool() as pool:
        result = pool.map(SumElement, [userList])
   
    print("Expected output: ")
        
    print("Sum of element is: ", result[0])  


if __name__ == "__main__":
    main()
