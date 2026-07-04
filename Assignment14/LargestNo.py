largestNo = lambda Value1, Value2, Value3: max(Value1, Value2, Value3)

def main():
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter Two number: "))
    No3 = int(input("Enter Two number: "))
    Largest = largestNo(No1,No2,No3)

    print("Largest of",No1,",",No3,"and",No2,"is: ",Largest)

if __name__ =="__main__":
    main()