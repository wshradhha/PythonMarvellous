import shutil

def main():
    try:
       shutil.copyfile("ABC.txt", "Demo.txt")
       print("File copied successfully!")
        
    except FileNotFoundError as fobj:
        print("file not present in the current directory")


if __name__ == "__main__":
    main()