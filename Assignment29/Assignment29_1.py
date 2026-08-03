import os

def main():

    file = input("Enter file name:")
    fobj = os.path.isfile(file)
    if(fobj):
        print("File Exist..")
    else:
        print("file not present in the current directory")

if __name__ == "__main__":
    main()