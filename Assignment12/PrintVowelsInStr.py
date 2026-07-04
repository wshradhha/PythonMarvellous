def ChkVowel(String):
    Vlist = []
    for i in String:
        if i in "AaEeIiOoUu":
            Vlist.append(i)
    return Vlist
    
def main():
    print("Enter A String: ")
    String = input()
    Ret = ChkVowel(String)
    if(len(Ret)==0):
        print("There is no Vowel...")
    else:
        print("List of Vowels available in String's are:- ",Ret)

if __name__ == "__main__":
    main()        
