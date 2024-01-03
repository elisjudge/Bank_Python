class Account:
    def __init__(self, name, starting_balance):
        self._name = name
        self._balance = starting_balance
    
    @property
    def name(self):
        return self._name
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount_to_add):
        print(f"Depositing ${amount_to_add}")
        self._balance += amount_to_add

    def withdraw(self, amount_to_subtract):
        print(f"Withdrawing ${amount_to_subtract}")
        self._balance -= amount_to_subtract

    def print_account(self):
        print(f"Account Name: {self.name}, Account Balance: ${self.balance}")