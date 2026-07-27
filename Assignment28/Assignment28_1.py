import os

def main():
    try:
        fobj = open("Demo.txt","r")
        print("file gets open")

        Data = fobj.readlines() #get list of lines read() will give char
        print(Data)
        cntLine = 0
        for i in Data:
            cntLine = cntLine + 1
        print("Total Lines are: ",cntLine)
        
    except FileNotFoundError as fobj:
        print("file not present in the current directory")


if __name__ == "__main__":
    main()