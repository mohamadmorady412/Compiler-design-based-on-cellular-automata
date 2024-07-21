import pygame
import numpy as np

# With the correct dimensions
class Environment_cd:
    def __init__(self, n_dime: int=0, Border_areas: int=0):
        self._number_moves = 2 * n_dime + 1
