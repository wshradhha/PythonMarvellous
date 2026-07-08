def ChkNo(No1):
    if(No1 >0):
        print(f"{No1} is Positive")
    elif(No1<0):
        print(f"{No1} is Negative")
    elif(No1 == 0):
        print(f"{No1} is Zero")
    
def main():
    Value1 = int(input("Enter a Number: ")) 

    Ret = ChkNo(Value1)

if __name__ == "__main__":
    main()