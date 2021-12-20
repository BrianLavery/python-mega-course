class Account:

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

account = Account("./balance_223.txt")
print(account) # If you run the file you get <main...> but if you import get <account...>
print(account.balance)
account.withdraw(100)
print(account.balance)
account.deposit(200)
print(account.balance)