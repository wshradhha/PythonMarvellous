
def factorial(No):
    fact = 1
    for i in range(1,No+1):
        fact = fact * i
    return fact

    
def main():
    Value1 = int(input("Enter first number: "))

    Fact = factorial(Value1)
    print(f"Factorial of {Value1} is {Fact}")
  

if __name__ == "__main__":
    main()