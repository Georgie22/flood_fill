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

    """
    Check a seed position is within the bounds of an image
    """

    if (seed.i >= 0 and seed.i < image_shape[0] and seed.j >=0 and seed.j < image_shape[1]):

        return True
    else:
        return False


def span_left(image: NDArray, seed: Type[SeedPoint], old_value: int, new_value: int) -> tuple[int, NDArray]:

    """
    Fill the scan line to the left of the seed point and return the image and the left-most filled position
    """

    lj = seed.j
    point = SeedPoint(seed.i, lj-1)

    while check_point_in_image(point, image.shape) and image[point.i, point.j] == old_value:
        image[point.i, point.j] = new_value
        lj = lj - 1
        point = SeedPoint(seed.i, lj-1)
    
    return lj, image


def span_right(image: NDArray, seed: Type[SeedPoint], old_value: int, new_value: int) -> tuple[int, NDArray]:

    """
    Fill the scanline to the right of the seed point and return the image and the right-most filled position
    """

    while check_point_in_image(seed, image.shape) and image[seed.i, seed.j] == old_value:
        image[seed.i, seed.j] = new_value
        seed.j += 1 
    
    return seed.j-1, image
    

def seed_search(lj, rj, i, stack):

    """
    Search for a seed point in the an adjacent row
    """
    pass


def span_fill(image: NDArray, initial_seed: Type[SeedPoint]) -> NDArray:

    """
    """

    # initialise stack
    stack = deque()
    if check_point_in_image(initial_seed, image.shape):
        stack.append(initial_seed)
    else:
        return IndexError

    # initialise values
    old_value = image[initial_seed.i, initial_seed.j]
    new_value = 1

    # fill loop
    while len(stack) != 0:
        seed = stack.pop()
        lj, image = span_left(image, seed, old_value, new_value)
        rj, image = span_right(image, seed, old_value, new_value)

    return image



def main():

    # create dummy image
    image = np.zeros((100,100))
    image[:, 15] = 1
    plt.imsave("original.png", image)

    initial_seed = SeedPoint(50,50)
    image = span_fill(image, initial_seed)
    plt.imsave("filled.png", image)
    


if __name__ == "__main__":
    main()