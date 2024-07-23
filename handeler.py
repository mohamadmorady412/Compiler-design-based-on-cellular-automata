#import importlib (---nextstation---)

import numpy as np
from math import factorial
from typing import Tuple


class Envarinment:
    def __init__(self, dime: Tuple[int, tuple[float], tuple[int]], sb: int, size: int, Type: str, ruls: dict) -> None:
        self.sb = sb
        self.size = size
        self.dime = dime
        self.type = Type

        match(Type):
            case 'integrete-dimension':
                self._n_dim = 2 * dime + 1
            case 'fractal-dimension':
                ...
            case _:
                base_intgrate_dimesion = ['integrete-dimension', 'id', 'numerical dimension']
                base_fractal_dimesion = ['fractal-dimension', 'fd', 'not-numerical-dimension']

                if Type in base_intgrate_dimesion:
                    ...
                elif Type in base_fractal_dimesion:
                    ...
                else:
                    raise ValueError('Unknown type: %s % Type')
            
        self._n_sb = factorial(sb)
        self._n_size = np.zeros(size)
    
    def c_randompattern(self,  problty: float=0.5, seed: int | None=None) -> np.asanyarray:
        if self.type == 'integrete dimension':
            if self._n_dim == 1:
                return np.zeros(1, dtype=np.int8)
            probaliteis = [True, False] * int(self._n_dim * problty)
            rng = np.random.default_rng(seed=seed)
            return rng.choice(probaliteis)

        else:
            ...
    
    def run(self):
        ...