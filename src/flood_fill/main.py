from typing import Type
from dataclasses import dataclass
from collections import deque

import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt


@dataclass
class SeedPoint():
    """Class to store the position of a seed"""
    i: int
    j: int


def check_point_in_image(seed: Type[SeedPoint], image_shape: tuple) -> bool:

    if (seed.i >= 0 and seed.i < image_shape[0] and seed.j >=0 and seed.j < image_shape[1]):
        return True
    else:
        return False



def fill_left(image: NDArray, seed: Type[SeedPoint], new_value: int) -> NDArray:
    pass


def fill_right():
    pass
    

def seed_search():
    pass


def span_fill(image: NDArray, initial_seed: Type[SeedPoint]):
    pass


def main():

    # create dummy image
    image = np.zeros((3,3))
    plt.imsave("original.png", image)



if __name__ == "__main__":
    
    main()