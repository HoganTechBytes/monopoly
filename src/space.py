'''
Board spaces and space types for a Monopoly-like game.

This module defines the types of spaces that can exist on the board
and the base Space data model used to represent them.
'''

from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional


class SpaceType(Enum):
    """
    Enumeration of different types of spaces on the Monopoly board.
    """
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
    """
    Represents a generic board space.
    """
    position: int
    name: str
    type: SpaceType


@dataclass
class PropertySpace(Space):
    """
    Represents a purchasable property or railroad.
    (Utilities are still plain Space for now.)
    """
    cost: int
    base_rent: int
    owner: Optional["Player"] = None
