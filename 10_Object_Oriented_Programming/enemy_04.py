class Enemy:
    def __init__(self, name="Enemy", hit_points=0, lives=1) -> None:
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_hp = self.hit_points - damage
        if remaining_hp >= 0:
            self.hit_points = remaining_hp
            print(f"{self.name} hit for {damage} damage!")
        else:
            self.lives -= 1

    def __str__(self) -> str:
        return f"{self.name} has {self.hit_points} hit points and {self.lives} lives left."
    

class Troll(Enemy):
    def __init__(self, name="Troll", hit_points=0, lives=1) -> None:
        super().__init__(name, hit_points, lives)