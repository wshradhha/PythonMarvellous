Add = lambda Value1, Value2: Value1 + Value2

def main():
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter Two number: "))
    Addition = Add(No1,No2)

    print("Addition of",No1,"and",No2,"is: ",Addition)

if __name__ =="__main__":
    main()