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
        if amount_to_add > 0:
            self._balance += amount_to_add
            return True
        return False

    def withdraw(self, amount_to_subtract):
        if amount_to_subtract <= self.balance and amount_to_subtract > 0:
            self._balance -= amount_to_subtract
            return True
        return False

    def print_account(self):
        print(f"Account Name: {self.name}, Account Balance: ${self.balance:,.2f}")