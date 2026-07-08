"""Bhai day 9 aur 10 ko chutti ki thi 🙂"""

# Inheritance is a way to form new classes using classes that have already been defined. The newly formed classes are called derived classes, the classes that we derive from are called base classes.
#Polymorphism is the ability to present the same interface for differing underlying forms (data types). Through polymorphism, each class can provide its own independent implementation of this interface.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def start(self):
        print(f"{self.name} is starting.")
    def stop(self):
        print(f"{self.name} is stopping.")

class Car(Vehicle):
    def __init__(self, name, max_speed, mileage, num_doors):
        super().__init__(name, max_speed, mileage)
        self.num_doors = num_doors
    def start(self): #this method overrides the start method of the Vehicle class called method overriding polymorphism
        print(f"{self.name} is starting with a roar!")
    def stop(self):
        print(f"{self.name} is stopping smoothly.")

class Bike(Vehicle):
    def __init__(self, name, max_speed, mileage, type_of_bike):
        super().__init__(name, max_speed, mileage)
        self.type_of_bike = type_of_bike
    def start(self):
        print(f"{self.name} is starting with a vroom!")
    def stop(self):
        print(f"{self.name} is stopping quickly.")


vehicle = Vehicle("Generic Vehicle", 100, 15)
car = Car("Toyota", 180, 12, 4)
bike = Bike("Harley-Davidson", 150, 10, "Cruiser")

vehicle.start()
vehicle.stop()
car.start()
car.stop()
bike.start()
bike.stop()


# Multiple Parents and Diamond Problem Solution is achieved through Method Resolution Order (MRO) in Python.

class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
class C(A):
    def show(self):
        print("C")
class D(B, C):
    pass

d = D()
d.show() #it has to print B because of MRO (Method Resolution Order) which is D -> B -> C -> A


# Dunder (magic) methods — make your classes behave like built-in types:
# __len__ → len(dataset) returns number of samples
# __getitem__ → dataset[0] returns first sample
# __repr__ → print(model) shows useful info
# __call__ → model(input) runs the forward pass
# PyTorch Dataset class requires you to implement __len__ and __getitem__.

"Will implmement dunder methods in the next exercise."