def AreaOfRect(Value1,Value2):
    Area = Value1 * Value2
    return Area
    
def main():
    print("Enter A Length: ")
    Len = int(input())

    print("Enter A Width: ")
    Width = int(input())
    Ret = AreaOfRect(Len,Width)

    print("Area of Rectangle is: ", Ret)

if __name__ == "__main__":
    main()        
