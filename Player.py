class Player():
    def __init__(self):
        self._score = 0

    def change_score(self, n):
        self._score += n

    @property
    def score(self):
        return self._score