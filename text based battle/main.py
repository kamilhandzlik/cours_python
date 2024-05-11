from character import character, Player, Enemy
from weapons import *

player = Player(name="Link", health=500)
player.equip(zweihander)
enemy = Enemy(name="Goblin", health=150, weapon=dagger)


while True:
    player.attack(enemy)
    enemy.attack(player)

    player.health_bar.update()
    enemy.health_bar.update()

    input()
