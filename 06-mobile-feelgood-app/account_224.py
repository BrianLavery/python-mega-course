class Account:
    # Call below a doc string - to explain class
    """This class generates a generic bank account"""
    def __init__(self, filepath):
        self.filepath = filepath # We are creating an instance variable to use elsewhere
        # We save data from file as instance variable
        with open(filepath, 'r') as file:
            self.balance = int(file.read()) # Need to convert to an int

    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.commit()

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.commit()
    
    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

# We do inheritance like below in Python - we pass in the parent class as a parameter
class Checking(Account):
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath) # This is calling the Account init
        self.fee = fee # Instance variable only for the subclass

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee
        self.commit()

checking = Checking("./balance_224.txt", 1)
print(checking)
print(checking.balance)
checking.deposit(10)
print(checking.balance)
checking.transfer(25)
print(checking.balance)