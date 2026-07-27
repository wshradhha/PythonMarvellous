import sys
import os
import hashlib

def CalculateCheckSum(Filename):

    fobj = open("Filename","rb")

    hobj = hashlib.ms5()

    Buffer = fobj.read(1000)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()
    return hobj.hexdigest()

def main():
    Ret = CalculateCheckSum("Demo.txt")
    print("Checksum of file is: ",Ret)

if __name__ == "__main()__":
    main()