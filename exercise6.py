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

    # def transfer_funds(self):


    # def 
    
def main():
        Regions = bank_branch("regions", "123 Sesame Street")
        action = 1
        while action != 6:
            print("""
            1.Create an account
            2. Check accounts
            3.
            4.
            5.
            6.Close the application
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
            elif action == 6:
                break

main()


