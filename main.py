# Design pattern implementation in python

# Creational Patterns

# Factory

class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)


class BurgerFactory:
    def create_cheese_burger(self):
        ingredients = ["bun", "cheese", "beef-patty"]
        return Burger(ingredients=ingredients)

    def create_deluxe_burger(self):
        ingredients = ["bun", "tomatoes", "lettuce"]
        return Burger(ingredients=ingredients)


burger_factory = BurgerFactory()
burger_factory.create_cheese_burger().print()
burger_factory.create_deluxe_burger().print()


# Builder
class Motor:
    def __init__(self):
        self.wheels = None
        self.brakes = None
        self.chain = None

    def set_wheels(self, wheels):
        self.wheels = wheels

    def set_brakes(self, brakes):
        self.brakes = brakes

    def set_chain(self, chain):
        self.chain = chain

    def list_part(self):
        print(f"Motor built with {self.brakes}, {self.chain} and {self.wheels}")


class MotorBuilder:
    def __init__(self):
        self.motor = Motor()

    def set_wheels(self, wheels):
        self.motor.set_wheels(wheels)
        return self

    def set_brakes(self, brakes):
        self.motor.set_brakes(brakes)
        return self

    def set_chain(self, chain):
        self.motor.set_chain(chain)
        return self

    def build(self):
        return self.motor


motor1 = MotorBuilder() \
        .set_brakes('brembo') \
        .set_chain('rcb') \
        .set_wheels('jrp') \
        .build()

print(motor1.list_part())
# Singleton


class ApplicationState:
    instance = None

    def __init__(self):
        self.isLoggedIn = False

    @staticmethod
    def get_app_state():
        if not ApplicationState.instance:
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance


app_state1 = ApplicationState.get_app_state()
print(app_state1.isLoggedIn)

app_state2 = ApplicationState.get_app_state()
app_state2.isLoggedIn = True

print(app_state2.isLoggedIn)
print(app_state1.isLoggedIn)


# Behavioral Patterns - PubSub
# Used in distributed system

# Observer
class YoutubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, sub):
        self.subscribers.append(sub)

    def notify(self, event):
        for sub in self.subscribers:
            sub.sendNotification(self.name, event)


# Define the subcriber interface
from abc import ABC, abstractmethod


class YoutubeSubscriber(ABC):
    @abstractmethod
    def sendNotification(self):
        pass


class YoutubeUser(YoutubeSubscriber):
    def __init__(self, name):
        self.name = name

    def sendNotification(self, channel, event):
        print(f"User {self.name} received notif from {channel}: {event}")


# Channels
ncode_channel = YoutubeChannel("ncode")
game_channel = YoutubeChannel("Namco")

# Users
edward = YoutubeUser("Edward")
ray = YoutubeUser("Ray")

# Subcribes
ncode_channel.subscribe(edward)
ncode_channel.subscribe(ray)

game_channel.subscribe(ray)

# Notify
ncode_channel.notify("A new course was released.")
game_channel.notify("A new game event was released")

# Iterator


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head
        self.cur = None

    # Define the Iterator
    def __iter__(self):
        self.cur = self.head
        return self

    # Iterate
    def __next__(self):
        if self.cur:
            val = self.cur.val
            self.cur = self.cur.next
            return val
        else:
            raise StopIteration


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
my_list = LinkedList(head)

for i in my_list:
    print(i)
