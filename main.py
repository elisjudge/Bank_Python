from enum import Enum

from account import Account
from depositTransaction import DepositTransaction
from withdrawTransaction import WithdrawTransaction
from transferTransaction import TransferTransaction


class MenuOption(Enum):
    DEPOSIT = 1
    WITHDRAW = 2
    TRANSFER = 3
    PRINT = 4
    QUIT = 5


def doDeposit(account):
    try:
        deposit_amount = float(input("Please enter the amount that you wish to deposit: "))
        transaction = DepositTransaction(account, deposit_amount)
        transaction.execute()
        transaction.print()
    except Exception as e:
        print(f"Exception: {e}")


def doWithdrawal(account):
    try:
        withdraw_amount = float(input("Please enter the amount that you wish to withdraw: "))
        transaction = WithdrawTransaction(account, withdraw_amount)
        transaction.execute()
        transaction.print()
    except Exception as e:
        print(f"Exception: {e}")


def doTransfer(from_account, to_account):
    try:
        transfer_amount = float(input(f"What amount will you be transferring to {to_account.name}?: "))
        transaction = TransferTransaction(from_account, to_account, transfer_amount)
        transaction.execute()
        transaction.print()
    except Exception as e:
        print(f"Exception: {e}")


def doPrint(account):
    account.print_account()


def main():
    account_01 = Account("John", 100.0)
    account_02 = Account("Mike", 100.0)

    while True:
        user_option = readUserOption()

        if user_option == MenuOption.DEPOSIT:
            doDeposit(account_01)
        elif user_option == MenuOption.WITHDRAW:
            doWithdrawal(account_01)
        elif user_option == MenuOption.TRANSFER:
            doTransfer(account_01, account_02)
        elif user_option == MenuOption.PRINT:
            doPrint(account_01)
            doPrint(account_02)
        elif user_option == MenuOption.QUIT:
            print("Quit")
            break


def readUserOption():
    while True:
        print("""\nChoose an option:
              1. Deposit Funds,
              2. Withdraw Funds,
              3. Transfer Funds,
              4. Show Account Balance,
              5. Quit """)
        
        try:
            option = int(input("Enter your choice (1-5): "))
            if option in range(1,6):
                return MenuOption(option)
            else:
                print("Invalid option. Please make sure that you select a valid option")
        except ValueError:
            print("Invalid input. Please enter a valid number option.")

if __name__ == "__main__":
    main()