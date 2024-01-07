from transaction import Transaction
from depositTransaction import DepositTransaction
from withdrawTransaction import WithdrawTransaction

class TransferTransaction(Transaction):
    def __init__(self, from_account, to_account, amount):
        super().__init__(amount)
        self._from_account = from_account
        self._to_account = to_account      
        self._the_withdraw = WithdrawTransaction(self._from_account, self._amount)
        self._the_deposit = DepositTransaction(self._to_account, self._amount)

    @property
    def succeeded(self):
        if self._the_withdraw.succeeded and self._the_deposit.succeeded:
            return True
        else:
            return False
            
    
    def execute(self):
        super().execute()
        
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
        super().rollback()
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