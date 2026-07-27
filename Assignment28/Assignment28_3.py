import os

def main():
    try:
        file = input("Enter file name:")
        fobj = open(file,"r")
        print("file gets open")

        Data = fobj.readlines()
        print(Data)

        for i in Data:
    
            print("Lines are: \n",i)
        
    except FileNotFoundError as fobj:
        print("file not present in the current directory")


if __name__ == "__main__":
    main()