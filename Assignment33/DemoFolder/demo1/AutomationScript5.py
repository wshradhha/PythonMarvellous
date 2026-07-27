
import sys
import os

def DirectoryScanner(DirectoryPath):
    print("Files from the Directory are:")
    for folderName, SubFolder, FileName in os.walk(DirectoryPath):
        for fname in FileName:
            print(fname)
def main():
    print("-"*50)
    print("Marvellous Automation System")
    print("-"*50)

    if len(sys.argv) == 2:
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is use to travel directory")
            print("For better usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as ")
            print("python filename.py DirectoryName")
            print("Directory name should be absolute path")
        else:
            DirectoryScanner(sys.argv[1])
    else:
        print("Invalid length of arguments")
        print("Print --h or --u for more information")

    print("-"*50)
    print("Thank you for using Marvellous Automation System")
    print("-"*50)

if __name__ == "__main__":
    main()