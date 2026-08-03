import os
import sys

def main():
    if len(sys.argv)==3:
        source_path = sys.argv[1]
        destination_path = sys.argv[2]
        try:

            if os.path.exists(source_path):

                fobj = open(source_path,"r")
                Data = fobj.read()

                Wobj = open(destination_path,"a")
                Wobj.write(Data)

                print(f"Successfully copied data from {source_path} to {destination_path}")

        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid arguments passed.")
        print(f"Usage: python {sys.argv[0]} <source_file> <destination_file>")

        

if __name__ == "__main__":
    main()