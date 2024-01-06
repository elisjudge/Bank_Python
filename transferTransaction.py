from depositTransaction import DepositTransaction
from withdrawTransaction import WithdrawTransaction

class TransferTransaction:
    def __init__(self, from_account, to_account, amount):
        self._from_account = from_account
        self._to_account = to_account
        self._amount = amount
        self._the_withdraw = WithdrawTransaction(self._from_account, self._amount)
        self._the_deposit = DepositTransaction(self._to_account, self._amount)
        self._executed = False
        self._reversed = False


    @property
    def executed(self):
        return self._executed
    

    @property
    def reversed(self):
        return self._reversed
    

    @property
    def succeeded(self):
        if self._the_withdraw.succeeded and self._the_deposit.succeeded:
            return True
        else:
            return False
            
    
    def execute(self):
        if self._executed:
            raise Exception("Transaction cannot be executed. It has aleady been executed.")
        
        self._the_withdraw.execute()
        if self._the_withdraw.succeeded:
            self._the_deposit.execute()
            if self._the_deposit.succeeded:
                self._executed = True
            else:
                self._the_withdraw.rollback()
        else:
            raise Exception("Cannot execute the deposit as the withdrawal was not successful")


    def rollback(self):
        if not self._executed:
            raise Exception("Cannot rollback this transaction. It has not been executed.")
        if self._reversed:
            raise Exception("Cannot rollback this transaction. It has already been reversed.")
        if self._the_withdraw.succeeded:
            self._the_withdraw.rollback()
        if self._the_deposit.succeeded:
            self._the_deposit.rollback()
        if self._the_withdraw.reversed and self._the_deposit.reversed:
            self._reversed = True    
        

    def print(self):
        if self._the_withdraw.succeeded and self._the_deposit.succeeded:
            print(f"Transfer of {self._amount} from {self._from_account.name}'s account to {self._to_account.name}'s account was successful.")
            self._the_withdraw.print()
            self._the_deposit.print()
        else:
            print("Transfer was not successful.")
            if self._reversed:
                print("Transfer was reversed.")