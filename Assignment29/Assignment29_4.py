import os
import sys

def main():
    if len(sys.argv)==3:
        source_path1 = sys.argv[1]
        source_path2 = sys.argv[2]
        try:

            if os.path.exists(source_path1) and os.path.exists(source_path2):

                fobj = open(source_path1,"r")
                Data1 = fobj.read()

                Wobj = open(source_path2,"r")
                Data2 = Wobj.read()

                if(Data1 == Data2):
                    print(f"Data from {source_path1} and {source_path2} matched")
                else:
                    print(f"Data from {source_path1} and {source_path2} not matched")

        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid arguments passed.")
        print(f"Usage: python {sys.argv[0]} <source_file> <destination_file>")

        

if __name__ == "__main__":
    main()