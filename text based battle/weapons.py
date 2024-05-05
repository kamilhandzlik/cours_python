class Weapon:
    def __init__(
        self,
        name: str,
        weapon_type: str,
        durability: int,
        lenght: int,
        damage: int,
        value: int,
    ) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.durability = durability
        self.max_durabolity = durability
        self.lenght = lenght
        self.damage = damage
        self.value = value

    def hit(self, hit: float):
        hit.durability -= 0.2
        hit.durability = max(hit.durability, 0)

        if hit.durabulity <= 0:
            print("your weapon have broken")


zweihander = Weapon(
    name="zweihander",
    weapon_type="sharp",
    durability=500,
    lenght=5,
    damage=50,
    value=250,
)
flamberg = Weapon(
    name="flamberg",
    weapon_type="sharp",
    durability=300,
    lenght=4,
    damage=42,
    value=200,
)
dagger = Weapon(
    name="dagger",
    weapon_type="sharp",
    durability=120,
    lenght=1,
    damage=33,
    value=250,
)
short_bow = Weapon(
    name="Short bow",
    weapon_type="ranged",
    durability=500,
    lenght=100,
    damage=48,
    value=250,
)
fists = Weapon(
    name="fists",
    weapon_type="blunt",
    durability=500,
    lenght=1,
    damage=10,
    value=0,
)
