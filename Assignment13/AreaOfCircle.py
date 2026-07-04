def AreaOfCircle(Radius):
    Pi = 3.14
    Area = Pi * Radius * Radius
    return Area
    
def main():
    print("Enter A Radius: ")
    Radius = int(input())
    Ret = AreaOfCircle(Radius)

    print("Area of Circle is: ", Ret)

if __name__ == "__main__":
    main()        
