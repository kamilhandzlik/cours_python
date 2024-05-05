from weapons import zweihander, flamberg, dagger, short_bow, fists


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
