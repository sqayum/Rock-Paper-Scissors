from random import randint
from Player import Player

class Computer(Player):
    @staticmethod
    def play() -> str:
        return "RPS"[randint(0, 2)]
