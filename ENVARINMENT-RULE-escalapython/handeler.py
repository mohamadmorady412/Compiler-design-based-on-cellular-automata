import pygame
import numpy as np
from collections import factorial

# With the correct dimensions
def Builder_infinite_degrees(number_free: int) -> list[tuple[int]]:
    controller_list = np.zeros(number_free, dtype=np.int8)
    

class Environment_cd:
    def __init__(self, n_dime: int, Border_areas: np.ndarray | None):
        """
        n_dime:
          It determines the non-fractal
          dimensions of the environment

        Border_areas:
          Determines whether the edges of the
          environment are killing or spawning
          if None then all env-moves is deadly
          else For each input number except one,
          it recognizes the number of edges of the 
          environment as spawning cells. 
        
        """
        self.n_dime = n_dime
        self._number_moves = 2 * n_dime + 1
        self._cervition = factorial(n_dime)

