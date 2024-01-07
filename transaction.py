from datetime import datetime as dt

class Transaction:
    def __init__(self, amount):
        self._amount = amount
        self._executed = False
        self._reversed = False

    @property
    def executed(self):
        return self._executed

    @property
    def reversed(self):
        return self._reversed
    
    @property
    def date_stamp(self):
        return self._date_stamp
    
    @property
    def succeeded(self):
        return
   
    def execute(self):
        if self._executed:
            raise Exception("Cannot execute this transaction as it has already been executed.") 
        self._executed = True
        self._date_stamp = dt.now()

    def rollback(self):
        if not self._executed:
            raise Exception("Cannot reverse a transaction that has not already been executed")
        if self._reversed:
            raise Exception("Cannot reverse a transaction that has already been reversed")
    
    def print(self):
        return