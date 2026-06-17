class Bank:
    def __init__(self,accNo,holderName,balance):
        self.accNo=accNo
        self.holderName=holderName
        self.balance=balance
        self.transaction=[]
    
    def deposit(self,amount):
        if amount<0:
            print("Insufficient Amount")
            return 
        self.balance+=amount
        self.transaction.append(f"Deposit Res.{amount}")
        print("Deposit Successfully")
        print("Current Balance After Deposit",self.balance)
    
    def Withdraw(self,amount):
        if amount>self.balance:
            print("Invalid Amount")
            return
        elif amount<0:
            print("Insufficient Amount")
            
        self.balance-=amount
        self.transaction.append(f"Withdrawl Res.{amount}")

        print("Withdrawl of",amount,"has been Successfully")
        print(" Balance After Wir=thdrawl :",self.balance)
    
    def Balance(self):
        print("Balance :",self.balance)  
   
    def display(self):
        print("Account No :",self.accNo)
        print("Account Holder :",self.holderName)
        print("Balance :",self.balance)
    
    def transactionHistory(self):
        if len(self.transaction)==0:
            print("No transaction Happen Yet!")
            return 
        
        for t in self.transaction:
            print(t)
            
    def transferMoney(self,s1,amount):
        if amount <0:
            print("Invalid Amount!")
            return
        
        elif amount > self.balance:
            print("Insufficent Amount!")
            return
            
       
        
        s1.balance+=amount
        self.balance-=amount
        self.transaction.append(f"Transferred Rs.{amount} to {s1.holderName}")
        s1.transaction.append(f"Received Rs.{amount} from {self.holderName}")
        print("Transferred Rs.",amount,"From ",s2.holderName," to",s1.holderName)
        print(s1.holderName ,":",s1.balance)
        print(self.holderName, ":",self.balance)
        
        
        

s1=Bank("101","Yasir ALi",75000) 
s2=Bank("213","Prem Perkash",40000) 
   
while True:
    print("===================")
    print("1.Deposit")
    print("2.Withdrawl")
    print("3.Check Balance")
    print("4.Display Account")
    print("5.Transfer Money")
    print("6.Show Transactions History")
    print("7.Exit")
    print("===================")

    choice=int(input("Enter the Choice :"))
    match choice:
      case 1:
            Amount=int(input("Enter the amount :"))
            s1.deposit(Amount)
      case 2:
           getmoney=int(input("Enter the amount to withdraw :"))
           s1.Withdraw(getmoney)
      case 3:
           s1.Balance()
      case 4:
           s1.display()
      case 5:
           Money=int(input("Enter the amount :"))
           s2.transferMoney(s1,Money)
      case 6:
           s1.transactionHistory()
      case 7:
          print("Thanks for your trust on ABL!")
          
          
          
        
    