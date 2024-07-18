class Bankaccount:
    def __init__(self,account_num,account_holder,balance=0):
        self.account_num = account_num
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return amount
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient amount!")
        else:
            self.balance-=amount
            return self.balance
    def get_balance(self):
        return self.balance

p1=Bankaccount(123456789,"SAMSON",2000)
x=p1.deposit(500)
e=p1.get_balance()
print(e)
r=p1.withdraw(2000)
print(r)
