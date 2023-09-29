class bank:
    def __init__(self,amo):
        self.static=amo
        self.balance=amo
    def withdraw(self,amo):
        self.balance=self.balance-amo
        self.static=self.static-amo
    def deposit(self,amo):
        self.balance=self.balance+amo
        self.static=self.static+amo
    def intrest(self):
        self.intres=((1/100)*self.static)
        self.balance=self.balance+self.intres
    def display(self):
        print(self.balance)
sai=bank(int(input()))
for i in range(1,13):
    if i!=5 and i!=9 and i!=12:
        sai.intrest()
    elif i==5:
        sai.withdraw(25000)
        sai.intrest()
    elif(i==9):
        sai.deposit(10000)
        sai.intrest()
    else :
        sai.intrest()       
        sai.display()
