import threading
import time

def CalculateCapitals(Str):
    count1 = 0
    for char in Str: 
        if char.isupper(): 
            count1 = count1 + 1
    print("Capital letters are:", count1)

def CalculateLower(Str):
    count2 = 0
    for char in Str:
        if char.islower():
            count2 = count2 + 1
    print("Lowercase letters are: ",count2)

def CalculateNumbers(Str):
    count3 = 0
    for char in Str:
        if char.isdigit():
            count3 = count3 + 1
    print("Numbers are: ",count3)

def main():
    print("Enter a String:")
    Value = input()

    Tobj1 = threading.Thread(target=CalculateCapitals, args=(Value,))
    Tobj2 = threading.Thread(target=CalculateLower, args=(Value,))
    Tobj3 = threading.Thread(target=CalculateNumbers, args=(Value,))

    Tobj1.start()
    Tobj2.start()
    Tobj3.start()

    Tobj1.join()
    Tobj2.join()
    Tobj3.join()

if __name__ == "__main__":
    main()


