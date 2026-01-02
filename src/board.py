'''
Board definitions and setup utilities for a Monopoly-like game.
'''

from space import Space, SpaceType, PropertySpace


def create_board():
    '''
    Create and return the full Monopoly game board.

    The list index corresponds to the position on the board (0-39).

    Returns:
        List[Space]: A list of Space / PropertySpace objects
        representing the game board.
    '''
    return [
        # 0
        Space(
            position = 0,
            name = "GO",
            type = SpaceType.GO
            ),

        # Brown
        PropertySpace(
            position = 1,
            name = "Mediterranean Avenue",
            type = SpaceType.PROPERTY,
            cost = 60,
            base_rent = 2,
        ),
        Space(
            position = 2,
            name = "Community Chest",
            type = SpaceType.COMMUNITY_CHEST
            ),
        PropertySpace(
            position = 3,
            name = "Baltic Avenue",
            type = SpaceType.PROPERTY,
            cost = 60,
            base_rent = 4,
        ),
        Space(
            position = 4,
            name = "Income Tax",
            type = SpaceType.TAX
            ),

        # Railroads
        PropertySpace(
            position = 5,
            name = "Reading Railroad",
            type = SpaceType.RAILROAD,
            cost = 200,
            base_rent = 25,
        ),

        # Light Blue
        PropertySpace(
            position = 6,
            name = "Oriental Avenue",
            type = SpaceType.PROPERTY,
            cost = 100,
            base_rent = 6,
        ),
        Space(
            position = 7,
            name = "Chance",
            type = SpaceType.CHANCE
            ),
        PropertySpace(
            position = 8,
            name = "Vermont Avenue",
            type = SpaceType.PROPERTY,
            cost = 100,
            base_rent = 6,
        ),
        PropertySpace(
            position = 9,
            name = "Connecticut Avenue",
            type = SpaceType.PROPERTY,
            cost = 120,
            base_rent = 8,
        ),

        Space(
            position = 10,
            name = "Jail / Just Visiting",
            type = SpaceType.JAIL
            ),

        # Pink
        PropertySpace(
            position = 11,
            name = "St. Charles Place",
            type = SpaceType.PROPERTY,
            cost = 140,
            base_rent = 10,
        ),
        Space(
            position = 12,
            name = "Electric Company",
            type = SpaceType.UTILITY
            ),
        PropertySpace(
            position = 13,
            name = "States Avenue",
            type = SpaceType.PROPERTY,
            cost = 140,
            base_rent = 10,
        ),
        PropertySpace(
            position = 14,
            name = "Virginia Avenue",
            type = SpaceType.PROPERTY,
            cost = 160,
            base_rent = 12,
        ),

        # Railroad
        PropertySpace(
            position = 15,
            name = "Pennsylvania Railroad",
            type = SpaceType.RAILROAD,
            cost = 200,
            base_rent = 25,
        ),

        # Orange
        PropertySpace(
            position = 16,
            name = "St. James Place",
            type = SpaceType.PROPERTY,
            cost = 180,
            base_rent = 14,
        ),
        Space(
            position = 17,
            name = "Community Chest",
            type = SpaceType.COMMUNITY_CHEST),
        PropertySpace(
            position = 18,
            name = "Tennessee Avenue",
            type = SpaceType.PROPERTY,
            cost = 180,
            base_rent = 14,
        ),
        PropertySpace(
            position = 19,
            name = "New York Avenue",
            type = SpaceType.PROPERTY,
            cost = 200,
            base_rent = 16,
        ),

        Space(
            position = 20,
            name = "Free Parking",
            type = SpaceType.FREE_PARKING
            ),

        # Red
        PropertySpace(
            position = 21,
            name = "Kentucky Avenue",
            type = SpaceType.PROPERTY,
            cost = 220,
            base_rent = 18,
        ),
        Space(
            position = 22,
            name = "Chance",
            type = SpaceType.CHANCE
            ),
        PropertySpace(
            position = 23,
            name = "Indiana Avenue",
            type = SpaceType.PROPERTY,
            cost = 220,
            base_rent = 18,
        ),
        PropertySpace(
            position = 24,
            name = "Illinois Avenue",
            type = SpaceType.PROPERTY,
            cost = 240,
            base_rent = 20,
        ),

        # Railroad
        PropertySpace(
            position = 25,
            name = "B&O Railroad",
            type = SpaceType.RAILROAD,
            cost = 200,
            base_rent = 25,
        ),

        # Yellow
        PropertySpace(
            position = 26,
            name = "Atlantic Avenue",
            type = SpaceType.PROPERTY,
            cost = 260,
            base_rent = 22,
        ),
        PropertySpace(
            position = 27,
            name = "Ventnor Avenue",
            type = SpaceType.PROPERTY,
            cost = 260,
            base_rent = 22,
        ),
        Space(
            position = 28,
            name = "Water Works",
            type = SpaceType.UTILITY
            ),
        PropertySpace(
            position = 29,
            name = "Marvin Gardens",
            type = SpaceType.PROPERTY,
            cost = 280,
            base_rent = 24,
        ),

        Space(
            position = 30,
            name = "Go To Jail",
            type = SpaceType.GO_TO_JAIL
            ),

        # Green
        PropertySpace(
            position = 31,
            name = "Pacific Avenue",
            type = SpaceType.PROPERTY,
            cost = 300,
            base_rent = 26,
        ),
        PropertySpace(
            position = 32,
            name = "North Carolina Avenue",
            type = SpaceType.PROPERTY,
            cost = 300,
            base_rent = 26,
        ),
        Space(
            position = 33,
            name = "Community Chest",
            type = SpaceType.COMMUNITY_CHEST
            ),
        PropertySpace(
            position = 34,
            name = "Pennsylvania Avenue",
            type = SpaceType.PROPERTY,
            cost = 320,
            base_rent = 28,
        ),

        # Railroad
        PropertySpace(
            position = 35,
            name = "Short Line Railroad",
            type = SpaceType.RAILROAD,
            cost = 200,
            base_rent = 25,
        ),

        Space(
            position = 36,
            name = "Chance",
            type = SpaceType.CHANCE
            ),

        # Dark Blue
        PropertySpace(
            position = 37,
            name = "Park Place",
            type = SpaceType.PROPERTY,
            cost = 350,
            base_rent = 35,
        ),
        Space(
            position = 38,
            name = "Luxury Tax",
            type = SpaceType.TAX
            ),
        PropertySpace(
            position = 39,
            name = "Boardwalk",
            type = SpaceType.PROPERTY,
            cost = 400,
            base_rent = 50,
        ),
    ]
