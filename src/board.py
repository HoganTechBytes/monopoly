'''
Board definitions and setup utilities for a Monopoly-like game.

'''

from space import Space, SpaceType
def create_board():
    '''
    Create and return the full Monopoly game board.

    The list index corresponds to the position on the board (0-39).

    Returns:
        List[Space]: A list of Space objects representing the game board.
    '''

    return [
        Space (position=0, name="GO", type=SpaceType.GO),
        Space (position=1, name="Mediterranean Avenue", type=SpaceType.PROPERTY),
        Space (position=2, name="Community Chest", type=SpaceType.COMMUNITY_CHEST),
        Space (position=3, name="Baltic Avenue", type=SpaceType.PROPERTY),
        Space (position=4, name="Income Tax", type=SpaceType.TAX),
        Space (position=5, name="Reading Railroad", type=SpaceType.RAILROAD),
        Space (position=6, name="Oriental Avenue", type=SpaceType.PROPERTY),
        Space (position=7, name="Chance", type=SpaceType.CHANCE),
        Space (position=8, name="Vermont Avenue", type=SpaceType.PROPERTY),
        Space (position=9, name="Connecticut Avenue", type=SpaceType.PROPERTY),
        Space (position=10, name="Jail / Just Visiting", type=SpaceType.JAIL),
        Space (position=11, name="St. Charles Place", type=SpaceType.PROPERTY),
        Space (position=12, name="Electric Company", type=SpaceType.UTILITY),
        Space (position=13, name="States Avenue", type=SpaceType.PROPERTY),
        Space (position=14, name="Virginia Avenue", type=SpaceType.PROPERTY),
        Space (position=15, name="Pennsylvania Railroad", type=SpaceType.RAILROAD),
        Space (position=16, name="St. James Place", type=SpaceType.PROPERTY),
        Space (position=17, name="Community Chest", type=SpaceType.COMMUNITY_CHEST),
        Space (position=18, name="Tennessee Avenue", type=SpaceType.PROPERTY),
        Space (position=19, name="New York Avenue", type=SpaceType.PROPERTY),
        Space (position=20, name="Free Parking", type=SpaceType.FREE_PARKING),
        Space (position=21, name="Kentucky Avenue", type=SpaceType.PROPERTY),
        Space (position=22, name="Chance", type=SpaceType.CHANCE),
        Space (position=23, name="Indiana Avenue", type=SpaceType.PROPERTY),
        Space (position=24, name="Illinois Avenue", type=SpaceType.PROPERTY),
        Space (position=25, name="B&O Railroad", type=SpaceType.RAILROAD),
        Space (position=26, name="Atlantic Avenue", type=SpaceType.PROPERTY),
        Space (position=27, name="Ventnor Avenue", type=SpaceType.PROPERTY),
        Space (position=28, name="Water Works", type=SpaceType.UTILITY),
        Space (position=29, name="Marvin Gardens", type=SpaceType.PROPERTY),
        Space (position=30, name="Go To Jail", type=SpaceType.GO_TO_JAIL),
        Space (position=31, name="Pacific Avenue", type=SpaceType.PROPERTY),
        Space (position=32, name="North Carolina Avenue", type=SpaceType.PROPERTY),
        Space (position=33, name="Community Chest", type=SpaceType.COMMUNITY_CHEST),
        Space (position=34, name="Pennsylvania Avenue", type=SpaceType.PROPERTY),
        Space (position=35, name="Short Line Railroad", type=SpaceType.RAILROAD),
        Space (position=36, name="Chance", type=SpaceType.CHANCE),
        Space (position=37, name="Park Place", type=SpaceType.PROPERTY),
        Space (position=38, name="Luxury Tax", type=SpaceType.TAX),
        Space (position=39, name="Boardwalk", type=SpaceType.PROPERTY),
    ]
