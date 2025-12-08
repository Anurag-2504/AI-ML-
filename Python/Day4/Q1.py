'''Q1 Create a class with BankAccount attributes account_number, owner_name
   and balance Add to and methods deposit, withdraw, check balance
'''

class BankAcount:
    def __init__(self,acc_number,owner_name,balance):
        self.acc_number=acc_number
        self.owner_name=owner_name
        self.balance=balance

    def deposite(self,amount):
        self.balance+=amount
        
    
    def withdraw(self,amount):
        self.balance-=amount
        
    
    def check_balance(self):
        print(f"Hi {self.owner_name}, welcome back!")
        print(f"Your current balance is : {self.balance}")
    
c1=BankAcount(101,"Anurag Ratna",1000)
c1.deposite(5000)
c1.check_balance()
c1.withdraw(2000)
c1.check_balance()
