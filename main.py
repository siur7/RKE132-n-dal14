from character import Hero, Villain
from file_utils import get_random_file_name

hero_name = get_random_file_name(r"data/heroes.txt")
hero_weapon = get_random_file_name(r"data/weapons.txt")
villain_name = get_random_file_name(r"data/villains.txt")
villain_weapon = get_random_file_name(r"data/weapons.txt")

hero = Hero(hero_name, hero_weapon)
villain = Villain(villain_name, villain_weapon)

print ("=== Battle begins! ===")

print(f"Hero:{hero.name} | HP: {hero.hp} | Weapon: {hero.weapon}")
print(f"Villain:{villain.name} | HP: {villain.hp} | Weapon: {villain.weapon}")

round_number = 1

while hero.is_alive() and villain.is_alive():
    print(f"--- Round {round_number} ---")

    hero.attack(villain)

    if not villain.is_alive():
        break

    villain.attack(hero)

    round_number = round_number + 1

print("=== Battle ends! ===")

if hero.is_alive():
    print("Hero saves the day!")
else:
    print("Dark side wins!")