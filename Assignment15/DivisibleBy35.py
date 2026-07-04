divisible = lambda No: No % 3 == 0 and No % 5 == 0

def main():
    Data = []
    print("how many No you want to enter: ")
    No = int(input())
    
    print("Enter No's: ")
    for i in range(No):
        Data.append(int(input()))
        
    print("Input Data is: ", Data)
    
    max_str = list(filter(divisible, Data))
    print("Strings with length >= 5: ", max_str)

if __name__ == "__main__":
    main()