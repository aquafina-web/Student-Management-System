
class BankAccount:
    name = ''
    __balance = 0

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    #deposit method
    def deposit(self, amount):
        self.__balance += amount

    #withdraw method
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount

    #getter method
    def get_balance(self):
        return self.__balance


name = input("Enter account holder name: ")
balance = int(input("Enter initial balance: "))

b1 = BankAccount(name, balance)

deposit_amount = float(input("Enter deposit amount: "))
b1.deposit(deposit_amount)

withdraw_amount = float(input("Enter withdraw amount: "))
b1.withdraw(withdraw_amount)

print(f"\nAccount Holder: {b1.name}")
print(f"Final Balance: {b1.get_balance()}")