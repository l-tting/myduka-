from datetime import datetime

today = datetime.today()
print(today)

        

class BankAccount:
    def __init__(self,acc_no,balance,owner_name,date_opened=today):
        self.account_number = acc_no
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner_name} deposited Ksh.{amount} to account: {self.account_number} \n New Balance is {self.balance}")
        else:
            print("Invalid amount entered,try again")


    def withdraw(self,amount):
        if amount > self.balance and amount < 0:
            print("Cannot complete withdrawal,invalid amount")
        else:
            self.balance -= amount
            print(f"{self.owner_name} has withdrawn Ksh.{amount} from account: {self.account_number} \n New Balance is {self.balance}")


    def display_info(self):
        print("-------My Bank Account Info-------")
        print(f"Acc No: {self.account_number}")
        print(f"Balance: {self.balance}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Date Opened: {self.date_opened}")


account1 = BankAccount("Acc001",0,"Jane")
account1.deposit(10000)
account1.withdraw(3000)
account1.display_info()