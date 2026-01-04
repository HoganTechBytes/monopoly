'''
    Player model for the Monopoly game.

    Defines the Player class and behavior for movement, money handling,
    and property ownership
'''
from dataclasses import dataclass, field
from typing import List, Optional

from space import PropertySpace


@dataclass
class Player:
    '''
    Represents a Monopoly player.
    '''
    name: str
    money: int = 1500
    position: int = 0
    in_jail: bool = False
    properties: List[PropertySpace] = field(default_factory=list)

    def move(self, steps: int) -> None:
        '''
        Move the player clockwise around the board.
        Awards $200 for passing GO.
        '''
        old_position = self.position
        self.position = (self.position + steps) % 40
        if self.position < old_position:
            print(f'{self.name} passed GO and collects $200.')
            self.money += 200

    def pay(self, amount: int, recipient: Optional["Player"] = None) -> None:
        '''
        Pay an amount to the bank or another player.
        (Bankruptcy rules not yet implemented.)
        '''
        self.money -= amount
        if recipient is not None:
            recipient.money += amount

    def receive(self, amount: int) -> None:
        '''
        Receive money from the bank.
        '''
        self.money += amount
