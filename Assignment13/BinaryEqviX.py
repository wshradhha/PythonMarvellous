import math

def BinaryEqvi(Value):
    if Value == 0:
        return "0"
        
    binary_str = ""
    while Value > 0:
        Rem = Value % 2
        Value = math.floor(Value / 2)
        binary_str = str(Rem) + binary_str
        
    return binary_str
    
def main():
    No = int(input("Enter A No: "))
    Ret = BinaryEqvi(No)
    print("Its binary number:", Ret)

if __name__ == "__main__":
    main()  