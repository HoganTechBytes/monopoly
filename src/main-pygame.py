'''
    Pygame front-end for Monopoly-like game.

    This version used the exisiting game logic and renders
    a very simple 2D board with tokens
'''

import sys
import pygame

from board import create_board
from player import Player
from game import roll_dice