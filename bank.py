class BankAccount(object):
    balance = 0
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return "Welcome %s your balance today is %.2f" % (self.name, self.balance)
    
    def show_balance(self):
        print("Your balance: %.2f" % self.balance)
    
    def deposit(self, amount):
        self.amount = amount
        if self.amount <= 0:
            print("The amount most be greater than zero")
            return
        elif self.amount > 0:
            print("Your deposit is: %.2f" % (self.amount) )
            self.balance += self.amount
            print(self.show_balance())

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Your withdraw overpass your balance")
            return
        else:
            print("You withdraw: %.2f" % (self.amount))
            self.balance -= self.amount
            print(self.show_balance())

my_account = BankAccount("Puchi")
print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account)