import sys
import os

def DirectoryTraverse(DirectoryName):
    exist = os.path.exists(DirectoryName)
    if(exist):
        for folderName,subfolderName,fileName in os.walk(DirectoryName):
            for fname in fileName:
                print(fname)
    else:
        print("Folder not exist")

def main():

    print("-"*50)
    print("File Automation System")
    print("-"*50)
    if len(sys.argv) == 2:
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("this script is used to travel Directory")
            print("For better usage please check --u flag")
            
        elif(sys.argv[1] == "--U" or sys.argv[1] == "--u"):
            print("Please execute the script as ")
            print("python filename.py DirectoryName")
            print("Directory name should be absolute path")
        else:
            DirectoryName = sys.argv[1]              #get folder
            print("Directory Name is: ",DirectoryName)
            DirectoryTraverse(DirectoryName)
    else:
        print("Invalid Arguments has passed")
        print("For more information use --h or --u")

    print("-"*50)
    print("Thank you for using File Automation System")
    print("-"*50)
if __name__ == "__main__":
    main()