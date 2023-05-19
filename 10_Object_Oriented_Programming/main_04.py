from player_04 import Player
from enemy_04 import Enemy, Troll

player_01 = Player("Okan")
random_monster_01 = Enemy("Basic enemy", 12, 1)
print(random_monster_01)

random_monster_01.take_damage(10)
print(random_monster_01)

random_monster_01.take_damage(10)
print(random_monster_01)

ugly_troll = Troll("Ugly troll")
print(ugly_troll)

another_troll = Troll("Another troll", 10, 1)
print(another_troll)

brother_troll = Troll("Brother troll", 23)
print(brother_troll)