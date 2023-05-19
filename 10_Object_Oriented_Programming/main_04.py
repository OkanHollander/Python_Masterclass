from player_04 import Player
from enemy_04 import Enemy

player_01 = Player("Okan")
random_monster_01 = Enemy("Basic enemy", 12, 1)
print(random_monster_01)

random_monster_01.take_damage(10)
print(random_monster_01)

random_monster_01.take_damage(10)
print(random_monster_01)