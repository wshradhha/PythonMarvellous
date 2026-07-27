import os

def main():
    try:
        file = input("Enter file name:")
        Text = input("Enter text which we have to find in file : ")
        fobj = open(file,"r")
        print("file gets open")

        Data = fobj.read()

        found = file.find(Text)
        if Text in Data:
            print(f"{Text} found in {file}")
        else:
            print(f"{Text} Not found in {file}")
        
    except FileNotFoundError as fobj:
        print("file not present in the current directory")


if __name__ == "__main__":
    main()