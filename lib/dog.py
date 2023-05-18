#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt", favourite_toy="Any"):
        self.name = name
        self.breed = breed
        self.favorite_toy = favourite_toy

    def bark(self):
        print("Woof!")

    def adopt(self, owner_name):
        self.owner = owner_name


fido = Dog('Fido')
# print(fido.name)
fido.owner = "Sophie"
print(fido.owner)
print(fido.breed)
print(fido.favorite_toy)

snoopy = Dog("Snoopy", "german", "Tennis Ball")
print(snoopy.name)
print(snoopy.breed)
print(snoopy.favorite_toy)
# print(snoopy.name)
