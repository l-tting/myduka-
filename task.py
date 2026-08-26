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




class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.brand} has started")


    def stop(self):
        print(f"{self.brand} has stopped")


    def display_info(self):
        print("-----vehicle info-----")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")



class Car(Vehicle):
    def __init__(self, brand, model, year,no_of_doors):
        super().__init__(brand, model, year)
        self.no_of_doors = no_of_doors


    def drive(self):
        super().start()
        print(f"{self.brand} {self.model} is driving")

    def stop(self):
        return super().stop()


    def display_info(self):
        super().display_info()
        print(f"No of doors: {self.no_of_doors}")


car1 = Car("Toyota","RAV4",2020,4)
car1.drive()
car1.stop()
car1.display_info()


class MotorCycle(Vehicle):
    def __init__(self, brand, model, year,engine_cc):
        super().__init__(brand, model, year)
        self.engine_cc = engine_cc

    def ride(self):
        super().start()
        print(f"{self.brand} is being ridden")

    def stop(self):
        return super().stop()

    def display_info(self):
        super().display_info()
        print(f"Engine size: {self.engine_cc}")

motor1 = MotorCycle("Honda","HA1",2023,1000)
motor1.ride()
motor1.stop()
motor1.display_info()