def AreaOfCircle(Value):
    Cnt = 0
    for i in range(1,Value):
        if(Value % i == 0):
            Cnt = Cnt + i
    return Cnt
    
def main():
    print("Enter A No: ")
    No = int(input())
    Ret = AreaOfCircle(No)
    if(Ret == No):
        print("Its perfect number: ", Ret)
    else:
        print("Its not perfect number")

if __name__ == "__main__":
    main()        
