from weapons import zweihander, flamberg, dagger, short_bow, fists
from health_bar import HealthBar


class character:
    def __init__(
        self,
        name: str,
        health: int,
    ) -> None:
        self.name = name
        self.health = health
        self.max_health = health

        self.weapon = fists

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update
        print(f"{self.name} dealt {self.weapon.damage} damage to {target.name}")


class Player(character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name, health)
        self.health_bar = HealthBar(self, color="green")

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} you have equiped {self.weapon.name}!")

    def drop(self) -> None:
        print(f"{self.name} dropped the {self.weapon}!")
        self.weapon = self.default_weapon


class Enemy(character):
    def __init__(self, name: str, health: int, weapon) -> None:
        super().__init__(name, health)
        self.health_bar = HealthBar(self, color="red")
        self.weapon = weapon
