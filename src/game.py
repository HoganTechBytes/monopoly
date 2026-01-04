'''
    Core gameplay utilities such as dice rolling
'''

import random
from typing import Tuple


def roll_dice() -> Tuple[int, bool, Tuple[int, int]]:
    '''
    Roll two six-sided dice.

    Returns:
        total: sum of the two dice
        doubles: True if both dice show the same value
        dice: (die1, die2)
    '''
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    total = d1 + d2
    doubles = d1 == d2
    return total, doubles, (d1, d2)
