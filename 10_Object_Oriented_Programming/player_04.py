class Player(object):
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self.score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("You can't have a negative lives")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self.score += delta * 1000
            self._level = level
        else:
            print("You can't have a negative level")
            

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    def __str__(self) -> str:
        return f"Name: {self.name}, Lives: {self.lives}, Level {self.level}, Score: {self.score}"
