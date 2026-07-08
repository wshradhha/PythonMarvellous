def ChkNum(No):
    if(No % 5 == 0):
        return True
    else:
        return False

def main():
    Value = int(input("Enter a Number: ")) 
    Ret = ChkNum(Value)
    if(Ret == True):
        print(f"{Value} is Divisible by 5")
    else:
        print(f"{Value} is not Divisible by 5")

if __name__ == "__main__":
    main()