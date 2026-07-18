import threading

def SumElement(myList,result1):
    sum = 0
    for i in myList:
        sum = sum + i
    result1['sum'] = sum
    return result1['sum']

def ProductElement(myList,result1):
    product = 1
    for num in myList:
        product = product * num  
    result1['product'] = product 
    return result1['product']
 
def main():
    userList = []
    print("Enter how many number you want in list: ")
    value = int(input())
    print("Enter elements in list: ")
    for i in range(value):
        userList.append(int(input()))
    result1 = {}
    Tobj1 = threading.Thread(target=SumElement, args=(userList,result1))
    Tobj2 = threading.Thread(target=ProductElement, args=(userList,result1))

    Tobj1.start()
    Tobj2.start()
    Tobj1.join()
    Tobj2.join()

        
    print("Sum of element is: ", result1['sum'])  
    print("Product of element is: ", result1['product'])  


if __name__ == "__main__":
    main()
