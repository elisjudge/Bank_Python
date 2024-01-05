from enum import Enum

from account import Account

class MenuOption(Enum):
    DEPOSIT = 1
    WITHDRAW = 2
    PRINT = 3
    QUIT = 4


def doDeposit(account):
    deposit_success = False

    while True:
        try:
            deposit_amount = float(input("Please enter the amount that you wish to deposit: "))
            break
        except ValueError:
            print("Please ensure that you are entering a valid deposit.")
        
    deposit_success = account.deposit(deposit_amount)

    if deposit_success:
        print("Deposit was successful.")
    elif not deposit_success:
        print("Deposit was not successful. Please use non-negative values")


def doWithdrawal(account):
    withdraw_success = False

    while True:
        try:
            withdraw_amount = float(input("Please enter the amount you wish to withdraw: "))
            break
        except ValueError:
            print("Please ensure that you are entering a valid withdrawal.")
    
    withdraw_success = account.withdraw(withdraw_amount)

    if withdraw_success:
        print("Withdrawal was successful.")
    elif not withdraw_success:
        print("Withdrawal was not successful")
        print("Please use non-negative values and ensure that value does not exceed account balance.")


def doPrint(account):
    account.print_account()


def main():
    account = Account("John", 100.0)

    while True:
        user_option = readUserOption()

        if user_option == MenuOption.DEPOSIT:
            doDeposit(account)
        elif user_option == MenuOption.WITHDRAW:
            doWithdrawal(account)
        elif user_option == MenuOption.PRINT:
            doPrint(account)
        elif user_option == MenuOption.QUIT:
            print("Quit")
            break


def readUserOption():
    while True:
        print("""\nChoose an option:
              1. Deposit Funds,
              2. Withdraw Funds,
              3. Show Account Balance,
              4. Quit """)
        
        try:
            option = int(input("Enter your choice (1-4): "))
            if option in range(1,5):
                return MenuOption(option)
            else:
                print("Invalid option. Please make sure that you select a valid option")
        except ValueError:
            print("Invalid input. Please enter a valid number option.")

if __name__ == "__main__":
    main()