from enum import Enum

from account import Account
from bank import Bank
from depositTransaction import DepositTransaction
from withdrawTransaction import WithdrawTransaction
from transferTransaction import TransferTransaction


class MenuOption(Enum):
    ADDACCOUNT = 1
    DEPOSIT = 2
    WITHDRAW = 3
    TRANSFER = 4
    PRINT = 5
    PRINTTRANSACTIONS = 6
    QUIT = 7


def doAddAccount(to_bank):
    while True:
        account_name = input("Please enter the account name: ")
        if account_name:
            break
    
    while True:
        try:
            opening_balance = float(input("Please enter the opening balance: "))
            if opening_balance < 0:
                raise Exception("Account balance cannot be negative number.")
            to_bank.add_account(Account(account_name, opening_balance))
            break
        except Exception as e:
            print(f"Exception: {e}")


def doDeposit(bank):
    account = findAccount(bank)
    if not account:
        return
    
    try:
        deposit_amount = float(input("Please enter the amount that you wish to deposit: "))
        deposit_transaction = DepositTransaction(account, deposit_amount)
        bank.execute_transaction(deposit_transaction)
        if not deposit_transaction.succeeded:
            raise Exception("Deposit was not successful.")
        deposit_transaction.print()
    except Exception as e:
        print(f"Exception: {e}")


def doWithdrawal(bank):
    account = findAccount(bank)
    if not account:
        return
    
    try:
        withdraw_amount = float(input("Please enter the amount that you wish to withdraw: "))
        withdraw_transaction = WithdrawTransaction(account, withdraw_amount)
        bank.execute_transaction(withdraw_transaction)
        if not withdraw_transaction.succeeded:
            raise Exception("Withdraw was not successful.")
        withdraw_transaction.print()
    except Exception as e:
        print(f"Exception: {e}")


def doTransfer(bank):
    try:
        from_account = findAccount(bank)
        if not from_account:
            return
        
        to_account = findAccount(bank)
        if not to_account:
            return
        
        if from_account == to_account:
            raise Exception("You cannot transfer between the same account.")
        
        try:
            transfer_amount = float(input(f"What amount will you be transferring to {to_account.name}?: "))
            transfer_transaction = TransferTransaction(from_account, to_account, transfer_amount)
            bank.execute_transaction(transfer_transaction)
            if not transfer_transaction.succeeded:
                raise Exception("Transfer was not successful.")
            transfer_transaction.print()
            
        except Exception as e:
            print(f"Exception: {e}")

    except Exception as e:
        print(f"Exception: {e}")


def doPrint(bank):
    account = findAccount(bank)
    if not account:
        return
    account.print_account()


def findAccount(from_bank):
    while True:
        name = input("Enter account name: ")
        if name:
            break
    
    result = from_bank.get_account(name)
    if not result:
        print(f"No account found with {name}.")
    return result


def main():
    bank = Bank()
    while True:
        user_option = readUserOption()

        if user_option == MenuOption.ADDACCOUNT:
            doAddAccount(bank)
        elif user_option == MenuOption.DEPOSIT:
            doDeposit(bank)
        elif user_option == MenuOption.WITHDRAW:
            doWithdrawal(bank)
        elif user_option == MenuOption.TRANSFER:
            doTransfer(bank)
        elif user_option == MenuOption.PRINT:
            doPrint(bank)
        elif user_option == MenuOption.PRINTTRANSACTIONS:
            bank.print_transaction_history()
        elif user_option == MenuOption.QUIT:
            print("Quit")
            break


def readUserOption():
    while True:
        print("""\nChoose an option:
              1. Add Account,
              2. Deposit Funds,
              3. Withdraw Funds,
              4. Transfer Funds,
              5. Show Account Balance,
              6. Show List of Transactions,
              7. Quit """)
        
        try:
            option = int(input("Enter your choice (1-7): "))
            if option in range(1,8):
                return MenuOption(option)
            else:
                print("Invalid option. Please make sure that you select a valid option")
        except ValueError:
            print("Invalid input. Please enter a valid number option.")


if __name__ == "__main__":
    main()