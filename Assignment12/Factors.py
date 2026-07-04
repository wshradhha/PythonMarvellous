def ChkVowel(Value):
    factors = []
    for i in range(1,Value+1):
        if(Value % i == 0):
            factors.append(i)
    return factors
    
def main():
    print("Enter A Number: ")
    No = int(input())
    Ret = ChkVowel(No)
    if(len(Ret)==0):
        print("There is no Vowel...")
    else:
        print("List of Vowels available in String's are:- ",Ret)

if __name__ == "__main__":
    main()        
