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


from datetime import datetime
print(datetime.now())