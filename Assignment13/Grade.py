def ChkGrade(ListOfMarcks):
    sum = 0
    for i in ListOfMarcks:
        sum = sum + i
    return sum
    
def main():
    print("Enter 5 marks: ")
    Len = []
    for i in range(1,6,1):
        Len.append(int(input()))

    Ret = ChkGrade(Len)

    if(Ret>=75):
        print("Distinction")
    elif(Ret>=60):
        print("First Class")
    elif(Ret>=50):
        print("Second Class")
    elif(Ret<50):
        print("Fail")

if __name__ == "__main__":
    main()        
