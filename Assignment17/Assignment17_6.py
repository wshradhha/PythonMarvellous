
def factorial(No):
    sum = 0
  
    for i in range(1,No):
        if(No % i ==0):
            sum = sum+i

    return sum

    
def main():
    Value1 = int(input("Enter first number: "))

    Fact = factorial(Value1)
    print(f"Sum of Factors of {Value1} is {Fact}")
  

if __name__ == "__main__":
    main()