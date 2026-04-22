import random

class Character:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

        self.hp = len(name) + 10

    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        self.hp = self.hp - damage

        if self.hp < 0:
            self.hp = 0

class Hero(Character):
    def __init__(self, name, weapon):
        super().__init__(name, weapon)

    def attack(self, other):
        damage = random.randint(0, len(self.weapon))

        if damage == 0:
            print(f"{self.name} attacks with {self.weapon}, but {other.name} dodges!")
        if damage > other.hp:
            print(f"{self.name} attacks with {self.weapon} for {damage} CRITICAL HIT!")
        else:
            print(f"{self.name} attacks with {self.weapon} for {damage}.")

        other.take_damage(damage)
        print(f"{other.name} has {other.hp} HP left.")

        heal = random.randint(0, 3)

        if heal > 0:
            self.hp = self.hp + heal
            print(f"{self.name} heals for {heal} HP and now has {self.hp} HP.")
        else:
            print()



class Villain(Character):
    def __init__(self, name, weapon):
        super().__init__(name, weapon)

    def attack(self, other):
        damage = random.randint(0, len(self.weapon) * 2)

        if self.hp < 5 and damage > 0:
            damage = damage + 2
        
        if damage == 0:
            print(f"{self.name} attacks with {self.weapon}, but {other.name} dodges!")

        if damage > other.hp:
            print(f"{self.name} attacks with {self.weapon} for {damage} CRITICAL HIT!")
        else:
            print(f"{self.name} attacks with {self.weapon} for {damage}.")

            other.take_damage(damage)
            print(f"{other.name} has {other.hp} HP left.\n")