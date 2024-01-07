class Bank:
    def __init__(self):
        self._accounts = []


    def add_account(self, account):
        self._accounts.append(account)


    def get_account(self, name):
        for account in self._accounts:
            if account.name.lower().strip() == name.lower().strip():
                return account
        return None


    def execute_transaction(self, transaction):
        transaction.execute()