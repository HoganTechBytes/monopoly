'''
    Player model for the Monopoly game.

    Defines the Player class and behavior for movement, money handling,
    and property ownership
'''
from dataclasses import dataclass, field

@dataclass
class Player:
    '''
        Represents a player for the Monopoly game

        Attributes:
            name (str): Displays player's name
            money (int): Current cash balance (default: 1500)
            position (int): Current board index (0-39)
            in_jail (bool): Jail status (default: False)
            properties (list): List of spaces owned by the player (default: empty list)
    '''
    name: str
    money: int = 1500
    position: int = 0
    in_jail: bool = False
    properties: list = field(default_factory = list)

    def move(self, steps: int):
        '''
            Move the Player forward by the given number of spaces.
            Handles passing 'Go' and collecting $200.

            Args:
                steps (int): Number of spaces to move forward.
        '''
        old_position = self.position
        self.position = (self.position + steps) % 40

        # Passed 'Go' logic
        if self.position < old_position:
            # Collect $200 for passing Go
            self.money += 200
            print(f"{self.name} collected $200 for passing Go!")

    def pay(self, amount: int, recipient = None):
        '''
            Pay money to the bank or another player.

            Args:
                amount (int): Amount of money to deduct.
                recipient (Player, optional): Player to receive the money. Defaults to None (bank).
        '''
        self.money -= amount
        if recipient:
            recipient.money += amount

    def receive(self, amount: int):
        '''
            Receive money from the bank or another player.

            Args:
                amount (int): Amount of money to add.
        '''
        self.money += amount
        