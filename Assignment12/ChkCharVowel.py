def ChkVowel(char):
   if char in "AaEeIiOoUu":
       print(char in "AaEeIiOoUu")
       return True
   else:
       return False
    
def main():
    char = input("Enter A Character")
    Ret = ChkVowel(char)
    if(Ret==True):
        print("Its a Vowel...")
    else:
        print("Its not Vowel...")


if __name__ == "__main__":
    main()        
