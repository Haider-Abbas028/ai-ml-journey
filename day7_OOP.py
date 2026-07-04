"OOP in Python "

#Defining classes in Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

P1=Person("Ali", 30)
print(P1.greet())
P2=Person("Ahmed", 25)
print(P2.greet())

# The "consenting Adults" philosophy: In OOP, we trust that the user of a class will use it correctly.
# We don't enforce strict access control like some other languages do.
# Instead, we rely on conventions and documentation to guide users on how to interact with our classes.

# Access Modifiers in Python
# publicvar | _protectedvar | __privatevar

"Getter and Setter Methods"
class User:
    def __init__ (self,):
        self.__username=input("Enter your username: ")
        self.__password=input("Enter your password: ")
#This is the modern way of creating getter and setter methods in Python using the @property decorator.
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, value):
        self.__username = value
    @username.deleter
    def username(self):
        del self.__username
    
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, value):
        if len(value) > 8:
            self.__password = value
        else:
            print("Password must be at least 8 characters long.")

User1=User()
L=True
while L:
    print("\n1. Change User1's username")
    print("2. Change User1's password")
    print("3. View User1's username and password")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        new_username = input("Enter new username for User1: ")
        User1.username = new_username
        print(f"User1's new username is: {User1.username}")

    if choice == 2:
        new_password = input("Enter new password for User1: ")
        User1.password = new_password
        print(f"User1's new password is: {User1.password}")

    if choice == 3:
        print(f"User1's username is: {User1.username}")
        print(f"User1's password is: {User1.password}")

    if (choice == 0 ):
        L=False
        print("Exiting...")



