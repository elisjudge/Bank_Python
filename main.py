from account import Account

def main():
    account = Account("John", 100)
    account.print_account()
    account.deposit(100)
    account.print_account()
    account.withdraw(50)
    account.print_account()
    account.deposit(100)
    account.print_account()
    account.withdraw(50)
    account.print_account()

if __name__ == "__main__":
    main()