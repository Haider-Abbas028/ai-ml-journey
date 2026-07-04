"Today we will be exploring static attributes and methods in Python classes. Static attributes are shared across all instances of a class, while static methods do not require an instance of the class to be called. Let's dive into some examples to understand how they work. Also , we will look at access modifiers in Python, which help us control the visibility of class attributes and methods. We will also explore getter and setter methods, which allow us to access and modify private attributes in a controlled manner. By the end of this session, you should have a good understanding of these concepts and how to implement them in your own classes."


class BankAccount:
    total_Accounts = 0  # Static attribute to keep track of total accounts

    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        BankAccount.total_Accounts += 1  # Increment total accounts when a new account is created

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")


    @staticmethod
    def get_total_accounts():
        return BankAccount.total_Accounts  # Static method to get the total number of accounts
    
    #protected and private methods
    def _protected_method(self):
        print("This is a protected method. It can be accessed within the class and its subclasses.")
    
    def __private_method(self):
        print("This is a private method. It can only be accessed within the class.")
    
# Example usage
account1 = BankAccount("123456", "Alice", 1000)
account2 = BankAccount("789012", "Bob", 1500)
account1.deposit(500)  # Deposited 500. New balance is 1500.
print(BankAccount.get_total_accounts())  # Output: 2

account1._protected_method()  # This is a protected method. It can be accessed within the class and its subclasses.
#account1.__private_method()  # This is a private method. It can only be accessed within the class.
"account1.__private_method() causes an AttributeError because private methods cannot be accessed directly from outside the class. However, we can access it using name mangling as shown below."
BankAccount._protected_method(account1)  # This is a protected method. It can be accessed within the class and its subclasses.
#BankAccount.__private_method(account1)  # This is a private method. It can only be accessed within the class.
"BankAccount.__private_method(account1) causes an AttributeError because private methods cannot be accessed directly from outside the class. However, we can access it using name mangling as shown below."
account1._BankAccount__private_method()  # This is a private method. It can only be accessed within the class.
BankAccount._BankAccount__private_method(account1)  # This is a private method. It can only be accessed within the class.