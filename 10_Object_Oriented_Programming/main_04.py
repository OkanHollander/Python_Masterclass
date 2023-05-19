from player_04 import Player

player_01 = Player('Okan')

print(player_01.name)
print(player_01.lives)
player_01.lives -= 1
print(player_01)

player_01.lives -= 1
print(player_01)

player_01.lives -= 1
print(player_01)

player_01.lives -= 1
print(player_01)

player_01.level += 8
print(player_01)

player_01.level -= 4
print(player_01)

player_01.score += 1
print(player_01)