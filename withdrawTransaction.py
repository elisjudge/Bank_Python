from transaction import Transaction

class WithdrawTransaction(Transaction):
    def __init__(self, account, amount):
        super().__init__(amount)
        self._account = account
        self._succeeded = False
    
    @property
    def succeeded(self):
        return self._succeeded
    
    def execute(self):
        super().execute()
        self._succeeded = self._account.withdraw(self._amount)


    def rollback(self):
        super().rollback()
        if self._account.deposit(self._amount):
            self._reversed = True
            self._executed = False
            self._succeeded = False
        else:
            self._reversed = False
            self._executed = True
            self._succeeded = True


    def print(self):
        if self._succeeded:
            print(f"You have withdrawn {self._amount} from {self._account.name}'s account")
        else:
            print("Your withdrawral was unsuccessful")
            if self._reversed:
                print("Withdraw was reversed.")