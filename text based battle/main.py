from character import character

hero = character(name="Link", health=100)
enemy = character(name="Goblin", health=60)


while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")

    input()
