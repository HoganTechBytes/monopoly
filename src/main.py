'''
    Entry point for running a text-based Monopoly game session.
'''

from typing import List, Optional

from board import create_board
from game import roll_dice
from player import Player
from space import SpaceType, PropertySpace


def run_auction(space: PropertySpace, players: List[Player]) -> None:
    '''
    Run an auction for an unowned property.

    All players may bid in turn. Highest valid bid wins, as long as the
    player can afford it. If no bids are placed, the property remains
    unowned.
    '''
    print(f'\nStarting auction for {space.name}.')
    print(f'(Face value is ${space.cost}, but bids can be any amount.)')

    highest_bid = 0
    winner: Optional[Player] = None

    while True:
        any_new_bid = False

        for p in players:
            max_possible = p.money
            if max_possible <= highest_bid:
                # Cannot beat current bid, skip this player
                continue

            raw = input(
                f'{p.name}, current highest is ${highest_bid}. '
                f'You have ${max_possible}. Enter bid or press Enter to pass: '
            ).strip()

            if not raw:
                continue

            try:
                bid = int(raw)
            except ValueError:
                print('Please enter a whole number.')
                continue

            if bid <= highest_bid:
                print(f'Bid must be greater than current highest (${highest_bid}).')
                continue

            if bid > max_possible:
                print(f'You cannot bid more than you have (${max_possible}).')
                continue

            highest_bid = bid
            winner = p
            any_new_bid = True
            print(f'{p.name} is now highest bidder at ${highest_bid}.')

        if not any_new_bid:
            break

    if winner is None:
        print(f'No one bid on {space.name}. It remains unowned.')
        return

    winner.pay(highest_bid)
    space.owner = winner
    winner.properties.append(space)
    print(f'{winner.name} wins {space.name} for ${highest_bid}.')
    print(f'{winner.name} now has ${winner.money} remaining.')


def handle_space(player: Player, space, players: List[Player]) -> None:
    '''
    Apply the effect of landing on a space.

    For now, supports:
      - PropertySpace: must either buy or send to auction; rent if owned.
      - Railroads: rent scales with number of railroads owned.
      - Tax spaces: simple flat tax.
      - Go To Jail: sends player to Jail.
      - Other spaces: simple placeholder messages.
    '''
    # Ownable property / railroad modeled as PropertySpace
    if isinstance(space, PropertySpace):
        if space.owner is None:
            print(f'{space.name} is unowned. Face value is ${space.cost}.')
            print(f'{player.name} has ${player.money}.')

            if player.money >= space.cost:
                choice = input(
                    'Buy it for face value? (y to buy, anything else to auction): '
                ).strip().lower()
                if choice.startswith('y'):
                    player.pay(space.cost)
                    space.owner = player
                    player.properties.append(space)
                    print(f'{player.name} bought {space.name} for ${space.cost}.')
                else:
                    print(f'{player.name} chose not to buy. Property goes to auction.')
                    run_auction(space, players)
            else:
                print(f'{player.name} cannot afford the face value. Property goes to auction.')
                run_auction(space, players)

        elif space.owner is player:
            print(f'{player.name} already owns {space.name}. Nothing happens.')
        else:
            owner = space.owner

            if space.type is SpaceType.RAILROAD:
                # Count how many railroads the owner has
                num_rr = sum(
                    1
                    for p in owner.properties
                    if isinstance(p, PropertySpace) and p.type is SpaceType.RAILROAD
                )
                rent_table = {1: 25, 2: 50, 3: 100, 4: 200}
                rent = rent_table.get(num_rr, 25)
                print(
                    f'{owner.name} owns {num_rr} railroad(s). '
                    f'Rent for landing on this railroad is ${rent}.'
                )
            else:
                # Regular colored properties use their base rent (no houses yet)
                rent = space.base_rent

            print(
                f'{player.name} must pay ${rent} in rent to '
                f'{owner.name} for landing on {space.name}.'
            )
            player.pay(rent, recipient=owner)
            print(f'{player.name} now has ${player.money}.')
            print(f'{owner.name} now has ${owner.money}.')

        return

    # Non-property spaces
    if space.type is SpaceType.GO:
        print('GO: Collect $200 when you pass (already handled on movement).')

    elif space.type is SpaceType.TAX:
        # Simple tax rule for now, based on name
        if 'Income' in space.name:
            amount = 200
        else:
            amount = 100
        print(f'{player.name} must pay ${amount} in tax.')
        player.pay(amount)
        print(f'{player.name} now has ${player.money}.')

    elif space.type is SpaceType.CHANCE:
        print(f'{player.name} draws a Chance card (not implemented yet).')

    elif space.type is SpaceType.COMMUNITY_CHEST:
        print(f'{player.name} draws a Community Chest card (not implemented yet).')

    elif space.type is SpaceType.JAIL:
        if player.in_jail:
            print(f'{player.name} is in Jail. (Jail rules not implemented yet.)')
        else:
            print(f'{player.name} is just visiting Jail.')

    elif space.type is SpaceType.GO_TO_JAIL:
        print(f'{player.name} is sent directly to Jail.')
        player.position = 10
        player.in_jail = True

    elif space.type is SpaceType.FREE_PARKING:
        print('Free Parking. Nothing happens.')

    elif space.type is SpaceType.UTILITY:
        print(f'{player.name} landed on a Utility (logic not implemented yet).')

    else:
        print('Nothing special happens on this space (yet).')


def main() -> None:
    '''
    Start and run the main game loop.

    Handles player turn rotation, dice rolls, movement, space lookup,
    property buying/auctions, rent, taxes, and basic doubles behavior.
    '''
    board = create_board()
    players: List[Player] = [
        Player('Player 1'),
        Player('Player 2'),
    ]

    current = 0
    play = True

    while play:
        player = players[current]
        print('\n' + '-' * 40)
        print(f"{player.name}'s turn. Money: ${player.money}")
        consecutive_doubles = 0

        while True:
            input(f"{player.name}, press Enter to roll...")

            roll, doubles, dice = roll_dice()
            print(f'Rolled {dice[0]} + {dice[1]} = {roll}.')

            if doubles:
                consecutive_doubles += 1
                print('Doubles! You get another roll (unless it is your third in a row).')
            else:
                consecutive_doubles = 0

            # Third consecutive doubles: go directly to Jail
            if consecutive_doubles == 3:
                print(f'{player.name} rolled doubles three times in a row!')
                print(f'{player.name} goes directly to Jail.')
                player.position = 10  # Jail position
                player.in_jail = True
                break  # end turn, no movement or property handling this roll

            # Normal move
            player.move(roll)
            space = board[player.position]

            print(f'{player.name} landed on {space.name}.')
            handle_space(player, space, players)

            if not doubles:
                # No extra roll; end this player's turn
                break

            # If we got here and it was doubles (but not 3rd in a row),
            # loop again to give the same player another roll.

        # Next player's turn
        current = (current + 1) % len(players)


if __name__ == '__main__':
    main()
    
