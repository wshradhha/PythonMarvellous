def isPrime(No):
    if(No<=1):
        return False
    elif(No ==2):
        return True
    elif(No>=2):
        for i in range(2,No+1):
            if(No % i == 0):
                return False
            else:
                return True

def main():
    Value = int(input("Enter a Number: "))
    prime = isPrime(Value)
   
    if(prime == True):
        print("No is prime")
    else:
        print("No is not prime")   

if __name__ == "__main__":
    main(); 