class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print(f"Account Holder {self.Name} and Current Balance {self.Amount}")

    def Deposite(self,depo_Amount):
        self.Amount = self.Amount + depo_Amount
        print("Updated balance is:")
        self.Display()

    def Withdraw(self,With_Amount):
        self.Amount = self.Amount - With_Amount
        print("Updated balance is:")
        self.Display()
    
    def CalculationInterest(self):
        Interest = (self.Amount * BankAccount.ROI)/100
        print(f"Interest received on balance is: {Interest}")

Bobj1 = BankAccount("Isha",5000)
Bobj1.Display()
Bobj1.Deposite(1000)
Bobj1.CalculationInterest()

Bobj2 = BankAccount("Ishanvi",3000)
Bobj2.Display()
Bobj2.Withdraw(500)
Bobj2.CalculationInterest()




