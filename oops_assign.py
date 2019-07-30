#bank account class
class BankAccount:
    
    bal=0
    def __init__(self):
        bal=0
        
    def Deposit(self):
        
        amt=float(input("Enter the amount to be deposited"))
        self.bal+=amt
        
        
    def checkBalance(self):
       print("\n Hello the new available balance is ",(self.bal))
           
    def withdraw(self):
        
        amt1=float(input("enter the amount needs to withdrawn"))
        self.bal-=amt1
        print("\n Hello the new available balance is ",(self.bal))
 #Minimum balance check class         
class MinAccBal(BankAccount):
    def withdraw(self):
        amt1=float(input("enter the amount needs to withdrawn"))
        if self.bal-amt1>5000:
            self.bal-=amt1 
            print("\n Hello the new available balance is ",(self.bal))
        else:
            print (" transaction cancelled due to minimum balance requirement of 5000")
            print("\n Hello the new available balance is ",(self.bal))
               
#calling the class       
obj1Anu= MinAccBal()
obj1Anu.Deposit() 
obj1Anu.checkBalance()
obj1Anu.withdraw()
             

               