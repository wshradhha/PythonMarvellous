import os

def main():
    try:
        file = input("Enter file name: ")
        String = input("Enter string: ")
        fobj = open(file,"r")
        print("file gets open")

        Data = fobj.read()
        cnt = Data.count(String)
        
        print(f"In file {file} we found {String} {cnt} Times")
        
    except FileNotFoundError as fobj:
        print("file not present in the current directory")


if __name__ == "__main__":
    main()