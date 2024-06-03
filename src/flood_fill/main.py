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
    Fill the scan line to the left of the seed point.

    Parameters: 
        image - 2D binary numpy array
        seed - starting position on scanline
        old_value - value to be replaced in fill
        new_value - value to fill with

    Returns:
        lj - position of the left-most filled pixel in the scanline
        image - image with scanline filled to the left of the seed
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
    Fill the scanline to the right of the seed point (including seedpoint)

    Parameters:
        image - 2D binary numpy array
        seed - starting position on scanline
        old_value - value to be replaced in fill
        new_value - value to fill with

    Return:
        (seed.j-1) - poaition of right-most filled pixel in scanline
        image - image with scanline filled to the right of the seed
    """

    while check_point_in_image(seed, image.shape) and image[seed.i, seed.j] == old_value:
        image[seed.i, seed.j] = new_value
        seed.j += 1 
    
    return seed.j-1, image
    

def seed_search(image: NDArray, lj: int, rj: int, i: int, stack: Type[deque], old_value:int) -> None:

    """
    Search for a seed point in the an adjacent scanline (row) and add to stack

    Parameters:
        image - binary numpy array
        lj - in previous scanline, what was the leftmost filled position
        rj - in the previous scanline, what was the rightmost filled position
        i - row index to search for seed (+/- 1 from previous scanline)
        stack - stack storing scanline seeds
        old_value - value to be replaced in fill
    """

    seed_added = False
    for j in range(lj, rj+1):
        seed = SeedPoint(i, j)
        if not check_point_in_image(seed, image.shape) or image[seed.i, seed.j] != old_value:
            seed_added = False
        elif not seed_added:
            stack.append(seed)
            seed_added = True

    return stack


def span_fill(image: NDArray, initial_seed: Type[SeedPoint]) -> NDArray:

    """
    Flood fill a 2D binary array from a seed point - one scanline at a time.

    Parameters:
        image - 2D binary numpy array
        initial seed - starting position for fill

    Returns:
        image - filled 
    """

    # initialise stack
    stack = deque()

    if check_point_in_image(initial_seed, image.shape):
        stack.append(initial_seed)
    else:
        return IndexError

    # initialise fill values
    old_value = image[initial_seed.i, initial_seed.j]
    new_value = 1

    # fill loop
    while len(stack) != 0:
        # scanline seed
        seed = stack.pop()

        # scanline fill
        lj, image = span_left(image, seed, old_value, new_value)
        rj, image = span_right(image, seed, old_value, new_value)

        # search for seeds in adjacent scanlines

        stack = seed_search(image, lj, rj, seed.i+1, stack, old_value)
        stack = seed_search(image, lj, rj, seed.i-1, stack, old_value)

    return image



def main():

    # create dummy image
    image = np.zeros((100,100))
    image[:, 25] = 1
    image[:, 75] = 1
    image[25, :] = 1
    image[75, :] = 1
    plt.imsave("original.png", image)

    initial_seed = SeedPoint(50,50)
    image = span_fill(image, initial_seed)
    plt.imsave("filled.png", image)
    


if __name__ == "__main__":
    main()