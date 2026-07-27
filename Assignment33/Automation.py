import sys
import os
import time

def DirectoryTraverse(DirectoryName):
    timestamp = time.ctime
    logfilename = 
    exist = os.path.exists(DirectoryName)
    
    if(exist):
        print("-"*50)

        print("Folder names are:- ")
        for folderName,subfolderName,fileName in os.walk(DirectoryName):
            for fname in fileName:
                print(fname)
        print("-"*50)
    else:
        print("Folder not exist")

def main():

    print("-"*50)
    print("File Automation System")
    print("-"*50)
    if len(sys.argv) == 4:
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("Duplicate file removal automation")
            print("This script scans a directory, identifies duplicate files using checksum, deletes duplicate files, created a log file and send the log file through email.")
            print("For better usage please check --u flag")
            
        elif(sys.argv[1] == "--U" or sys.argv[1] == "--u"):
            print("Please execute the script as ")
            print("python filename.py <AbsoluteDirectoryPath><TimeIntervalInMinutes><ReceiverEmailAddress>")
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