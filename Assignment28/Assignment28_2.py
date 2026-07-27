import os

def main():
    try:
        file = input("Enter file name:")
        fobj = open(file,"r")
        print("file gets open")

        Data = fobj.read()
        print(Data)
        words = Data.split()
        cntWords = 0
        for i in words:
            cntWords = cntWords + 1
        print("Total Lines are: ",cntWords)
        
    except FileNotFoundError as fobj:
        print("file not present in the current directory")


if __name__ == "__main__":
    main()