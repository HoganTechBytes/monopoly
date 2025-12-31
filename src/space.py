'''
Board spaces and space types for a Monopoly-like game.

This module defines the types of spaces that can exist on the board
and the base Space data model used to represent them.
'''

from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, List, Dict

class SpaceType(Enum):
    '''
    Enumeration of different types of spaces on the board.

    These are used to determine how a player should interact with a
    space when they land on it.
    '''

    GO = auto()
    PROPERTY = auto()
    RAILROAD = auto()
    UTILITY = auto()
    TAX = auto()
    CHANCE = auto()
    COMMUNITY_CHEST = auto()
    JAIL = auto()
    GO_TO_JAIL = auto()
    FREE_PARKING = auto()

@dataclass
class Space:
    '''
    Represents a single space on the game board.

    Attributes:
        position (int): The position of the space on the board (0-39).
        name (str): The name of the space.
        type (SpaceType): The type of the space, as defined in SpaceType enum.
    '''
    position: int
    name: str
    type: SpaceType

@dataclass
class PropertySpace(Space):
    '''
    Represents a property space on the board.

    Attributes:
        cost: Purchase price of the property
        base_rent: Rent before any houses/hotels
        owner: Player who owns the property, None if unowned
    '''

    cost: int
    base_rent: int
    owner: Optional["Player"] = None

