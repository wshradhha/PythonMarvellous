def ChkNum(No):
    if(No % 2 == 0):
        return True
    else:
        return False

def main():
    Value = int(input("Enter a Number: ")) 
    Ret = ChkNum(Value)
    if(Ret == True):
        print(f"{Value} is Even Number")
    else:
        print(f"{Value} is Odd Number")

if __name__ == "__main__":
    main()