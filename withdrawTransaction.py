class WithdrawTransaction:
    def __init__(self, account, amount):
        self._account = account
        self._amount = amount
        
        self._executed = False
        self._succeeded = False
        self._reversed = False


    @property
    def succeeded(self):
        return self._succeeded
    
    
    @property
    def executed(self):
        return self._executed
    

    @property
    def reversed(self):
        return self._reversed
    

    def execute(self):
        if self._executed:
            raise Exception("Cannot execute this transaction as it has already been executed")
        self._executed = True
        self._succeeded = self._account.withdraw(self._amount)


    def rollback(self):
        if not self._executed:
            raise Exception("Cannot reverse a transaction that has not already been executed")
        if self._reversed:
            raise Exception("Cannot reverse a transaction that has already been reversed")
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