from typing import Tuple
from itertools import permutations

class RPSDecisionMaker():
    _MOVE_TYPES = "RPS"

    _MOVE_COMBINATIONS = [''.join(move_combination) for move_combination in permutations(_MOVE_TYPES, r=2)]
    _MOVE_COMBINATIONS.extend(code*2 for code in _MOVE_TYPES)


    _SCORE_LOOKUP = {}
    for move_combination in _MOVE_COMBINATIONS:
        if move_combination[0] == 'R':
            if move_combination[1] == 'P':
                _SCORE_LOOKUP[move_combination] = (0, 1)
            elif move_combination[1] == 'S':
                _SCORE_LOOKUP[move_combination] = (1, 0)
            else:
                _SCORE_LOOKUP[move_combination] = (0, 0)

        elif move_combination[0] == 'P':
            if move_combination[1] == 'S':
                _SCORE_LOOKUP[move_combination] = (0, 1)
            elif move_combination[1] == 'R':
                _SCORE_LOOKUP[move_combination] = (1, 0)
            else:
                _SCORE_LOOKUP[move_combination] = (0, 0)

        else:
            if move_combination[1] == 'R':
                _SCORE_LOOKUP[move_combination] = (0, 1)
            elif move_combination[1] == 'P':
                _SCORE_LOOKUP[move_combination] = (1, 0)
            else:
                _SCORE_LOOKUP[move_combination] = (0, 0)

    @classmethod
    def decide_outcome(cls, moves_played: str) -> Tuple[int, int]:
        if moves_played in cls._SCORE_LOOKUP:
            return cls._SCORE_LOOKUP[moves_played]
        else:
            return (-1, 0)