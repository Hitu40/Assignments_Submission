class Dog:
    def _init_(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def bark(self):
        print("Woof! Woof!")

    def hunt(self):
        print(f"{self.name} is hunting.")


class Bulldog(Dog):
    def _init_(self, name, age, coat_color, weight):
        super()._init_(name, age, coat_color)
        self.weight = weight

    def run(self):
        print(f"{self.name} is running.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color} and weight is {self.weight} kg.")


# create objects and call the methods
dog1 = Dog("Max", 3, "brown")
dog1.description()
dog1.get_info()

dog2 = JackRussellTerrier("Rocky", 5, "white and brown")
dog2.description()
dog2.get_info()
dog2.bark()
dog2.hunt()

dog3 = Bulldog("Buddy", 2, "gray", 30)
dog3.description()
dog3.get_info()
dog3.run()