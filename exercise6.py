####Med HW exercise for 1/22
class bank_account():
    def __init__(self, fname, lname, mname, account_type, balance, status):
        self.fname = fname 
        self.lname = lname
        self.mname  = mname 
        self.account_type = account_type
        self.balance = balance
        self.status = status

class bank_branch():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.accounts = []
    
    def add_account(self, fname, lname, mname, account_type, balance, status):
        if balance >= 100:
            temp = bank_account(fname, lname, mname, account_type, balance, status)
            self.accounts.append(temp)
            return(print(f"Account created for {fname} {lname}"))
        else:
            return(print("Insufficent ammount to open an account"))
    
    def show_current_accounts(self):
        for account_objects in self.accounts:
            print(f"{account_objects.fname} {account_objects.mname} {account_objects.lname}, {account_objects.account_type} account, balance of ${account_objects.balance}, the status of the account is: {account_objects.status}")

    def transfer_funds(self, original_account, second_account, trans_ammount):
        for accounts in self.accounts:
            if accounts.fname == original_account:
                accounts.balance -= trans_ammount
                if accounts.balance < 0:
                    accounts.balance -= 35
            if accounts.fname == second_account:
                accounts.balance += trans_ammount
    
    def withdraw_funds(self, account_to_withdraw, withdraw_ammount):
        for accounts in self.accounts:
            if accounts.fname == account_to_withdraw:
                accounts.balance -= withdraw_ammount
                if accounts.balance < 0:
                    accounts.balance -= 35

def main():
        Regions = bank_branch("regions", "123 Sesame Street")
        action = 1
        while action != 5:
            print("""
            1.Create an account
            2.Check accounts
            3.Transfer funds
            4. Withdraw funds
            5.Close the application
            """)
            action = int(input("What action would you like to take? "))
            if action == 1:
                fname = input("what is the first name? ")
                lname =  input("what is your last name? ")
                mname = input("What is your middle name?")
                account_type = input("What kind of account would you like to open? ")
                deposit = int(input("How much would you like to deposit? "))
                account_status = input("Status? ")
                Regions.add_account(fname, lname, mname, account_type, deposit , account_status)
            elif action == 2:
                Regions.show_current_accounts()
            elif action == 3:
                original_account = input("What the first name on the account you'd like to transfer FROM? ")
                second_account = input("What is your first name on the account you'd like to transfer TOO? ")
                trans_ammount= int(input("How much would you like to transfer? "))
                Regions.transfer_funds(original_account, second_account, trans_ammount)
                print(f"You transfered ${trans_ammount} from {original_account}to {second_account}")
            elif action == 4:
                account_to_withdraw= input("What the first name on the account you'd like to withdraw from?  ")
                withdraw_ammount = int(input("How much would you like to withdraw? "))
                Regions.withdraw_funds(account_to_withdraw, withdraw_ammount)
                print(f"You withdrew ${withdraw_ammount} from {account_to_withdraw}.")
            elif action == 5:
                break

main()


