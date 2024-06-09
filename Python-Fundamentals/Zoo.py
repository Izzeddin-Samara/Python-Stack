class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, animal):
        self.animals.append(animal)
        return self

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.display_info()

class Animal:
    def __init__(self, name, age, health=100, happiness=100):
        self._name = name
        self._age = age
        self._health = health
        self._happiness = happiness

    # Getter methods
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_health(self):
        return self._health

    def get_happiness(self):
        return self._happiness

    # Setter methods
    def set_health(self, value):
        if 0 <= value <= 100:
            self._health = value

    def set_happiness(self, value):
        if 0 <= value <= 100:
            self._happiness = value

    def display_info(self):
        print(f"Name: {self.get_name()}, Age: {self.get_age()}, Health: {self.get_health()}, Happiness: {self.get_happiness()}")
        return self

    def feed(self):
        self.set_health(min(100, self.get_health() + 10))
        self.set_happiness(min(100, self.get_happiness() + 10))
        return self


class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=90, happiness=80)
        self.mane_size = "Large"

    def display_info(self):
        super().display_info()
        print(f"Mane Size: {self.mane_size}")
        return self

    def feed(self):
        super().feed()
        self.set_health(min(100, self.get_health() + 5))  # Lions are tough, so feeding them gives a smaller boost
        return self


class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=85, happiness=90)
        self.stripe_pattern = "Striped"

    def display_info(self):
        super().display_info()
        print(f"Stripe Pattern: {self.stripe_pattern}")
        return self

    def feed(self):
        super().feed()
        self.set_health(min(100, self.get_health() + 8))  # Tigers are big eaters, so feeding them gives a bigger boost
        return self


class Bear(Animal):
    def __init__(self, name, age, fur_color="Brown"):
        super().__init__(name, age, health=95, happiness=85)
        self.fur_color = fur_color

    def display_info(self):
        super().display_info()
        print(f"Fur Color: {self.fur_color}")
        return self

    def feed(self):
        super().feed()
        self.set_health(min(100, self.get_health() + 7))  # Bears are hearty eaters, so feeding them gives a moderate boost
        return self


# Creating a Zoo and adding animals with method chaining
zoo1 = Zoo("John's Zoo")
zoo1.add_animal(Lion("Nala", 5)).add_animal(Lion("Simba", 6)).add_animal(
    Tiger("Rajah", 4)).add_animal(Tiger("Shere Khan", 7)).add_animal(Bear("Baloo", 8))

# Testing feed method with method chaining
for animal in zoo1.animals:
    animal.feed()

# Printing info of all animals in the zoo
zoo1.print_all_info()
