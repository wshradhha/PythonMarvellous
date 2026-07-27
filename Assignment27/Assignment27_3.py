class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
       
        if self.Value <= 1:
            print(f"{self.Value} is Not Prime")
            return
            
        isPrime = True
      
        for i in range(2, int(self.Value**0.5) + 1):
            if self.Value % i == 0:
                isPrime = False
                break 
                
        if isPrime:
            print(f"{self.Value} is Prime")
        else:
            print(f"{self.Value} is Not Prime")

    def ChkPerfect(self):
        
        if self.Value <= 1:
            print(f"{self.Value} is Not Perfect Number")
            return

        total_sum = 1  
        for i in range(2, self.Value):
            if self.Value % i == 0: 
                total_sum += i
                
        if self.Value == total_sum:
            print(f"{self.Value} is Perfect Number")
        else:
            print(f"{self.Value} is Not Perfect Number")

    def Factors(self):
        fact = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                fact.append(i)
        print(f"Factors of number {self.Value} are {fact}")

    def SumOfFactors(self):
        total_sum = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0: 
                total_sum += i
        print(f"Sum of Factors of number {self.Value} is {total_sum}")

Nobj1 = Numbers(13)
Nobj1.ChkPerfect()
Nobj1.ChkPrime()
Nobj1.Factors()
Nobj1.SumOfFactors()

Nobj2 = Numbers(40)
Nobj2.ChkPerfect()
Nobj2.ChkPrime()
Nobj2.Factors()
Nobj2.SumOfFactors()
