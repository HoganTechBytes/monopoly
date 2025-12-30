'''
    Core gameplay utilities such as dice rolling
'''

import random

def roll_dice():
    '''
        Roll two six-sided dice.

        Returns:
            total (int): Sum of both dice.
            doubles (bool): True if both dice show the same number.
            dice (tuple): The raw die results (d1, d2).
    '''
    d1 = random.randint (1,6)
    d2 = random.randint(1,6)
    doubles = d1 == d2
    return d1 + d2, doubles, (d1, d2)
