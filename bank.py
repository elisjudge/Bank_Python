class Bank:
    def __init__(self):
        self._accounts = []
        self._transactions = []


    def add_account(self, account):
        self._accounts.append(account)


    def get_account(self, name):
        for account in self._accounts:
            if account.name.lower().strip() == name.lower().strip():
                return account
        return None


    def execute_transaction(self, transaction):
        transaction.execute()
        self._transactions.append(transaction)


    def print_transaction_history(self):
        for transaction in self._transactions:
            transaction.print()
