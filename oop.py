# Base class 
# Polymorphism
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Function that accepts Animal type and calls speak function
def animal_sound(animal: Animal):
    print(animal.speak())


dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)


# Defining a class

class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def display_details(self):
        print(f'Car Make: {self.make}')
        print(f'Car Model: {self.model}')
        print(f'Car Color: {self.color}')

    def honk(self):
        print("Honk, Honk")


# Inheritance
class ElectricCar(Car):
    def __init__(self, make, model, color, battery_size):
        super().__init__(make, model, color)
        self.battery_size = battery_size

    def display_details(self):
        super().display_details()
        print(f'Car Battery size: {self.battery_size}')


car1 = Car("Toyota", "Trueno", "Panda")
car2 = Car("Nissan", "GTR", "Black")

car3 = ElectricCar("Tesla", "Model S", "White", 100)


car1.display_details()
car2.display_details()
car3.display_details()


# Polymorphism with interface
class Vehicle:
    def move(self):
        print("Vehicle is moving")


class Boat(Vehicle):
    def move(self):
        print("Boat is cruising")


class Bike(Vehicle):
    def move(self):
        print("Bike is cycling")


v1 = Boat()
v2 = Bike()


def start_journey(vehicle: Vehicle):
    vehicle.move()


start_journey(v1)
start_journey(v2)


# Encapsulation
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Amount was debited current balance: {self.__balance}')
        else:
            print("Amount was invalid must be positive value")

    def withdraw(self, amount):
        self.__balance -= amount
        print(f'Amount was withdrawn current balance: {self.__balance}')

    def get_balance(self):
        print(f'Current balance: {self.__balance}')


acc1 = BankAccount("Ed", 100000)
acc2 = BankAccount("Ray", 2000)

acc1.withdraw(200)
acc2.deposit(20000000)
