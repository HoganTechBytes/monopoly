'''
    Entry point for running a text-based Monopoly game session.
'''

from player import Player
from board import create_board
from game import roll_dice

def main():
    '''
        Start and run the main game loop.

        Handles player turn rotation, dice rolls, movement, and space lookup.

        TODO: Implement game rules for each space type
            - Property
            - Comunity Chest
            - Chance
            - Go to jail
            - Free Parking (nothing to do here, really)
            - Jail/Just Visiting
    '''

    board = create_board()
    players = [
        Player('Player 1'),
        Player('Player 2')
    ]

    current = 0
    play = True

    while play:
        player = players[current]
        input(f"{player.name}'s turn. Press Enter to roll...")

        roll, doubles, dice = roll_dice()
        print(f'Rolled {dice[0]} + {dice[1]} = {roll}.')

        player.move(roll)
        space = board[player.position]

        print(f'{player.name} landed on {space.name}.')

        #TODO: Implement space behavior rules below

        current = (current + 1) % len(players)

if __name__ == '__main__':
    main()
