def ChkVowel(String):
    Cnt = 0
    for i in String:
        if i in "AaEeIiOoUu":
            Cnt = Cnt + 1
    return Cnt
    
def main():
    String = input("Enter A String")
    Ret = ChkVowel(String)
    if(Ret==0):
        print("There is no Vowel...")
    else:
        print("Count of Vowel is:- ",Ret)

if __name__ == "__main__":
    main()        
