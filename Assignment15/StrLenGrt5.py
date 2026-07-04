get_length = lambda text: len(text) >= 5

def main():
    Data = []
    print("how many No you want to enter: ")
    No = int(input())
    
    print("Enter No's: ")
    for i in range(No):
        Data.append(input())
        
    print("Input Data is: ", Data)
    
    max_str = list(filter(get_length, Data))
    print("Strings with length >= 5: ", max_str)

if __name__ == "__main__":
    main()