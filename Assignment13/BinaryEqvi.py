import math

def BinaryEqvi(Value):
   # list = []
    Binary = ""
    while(Value):
        Rem = Value % 2
        Value = math.floor(Value/2)
        #list.append(Rem)
        Binary = str(Rem) + Binary
    #return list
    return Binary
    
def main():
    print("Enter A No: ")
    No = int(input())
    Ret = BinaryEqvi(No)
    print("Its perfect number: ", Ret)

if __name__ == "__main__":
    main()        

