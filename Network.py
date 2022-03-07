import numpy as np
import random


class Network:

    size = 0
    add_weights = np.array([])
    subtract_weights = np.array([])
    multiply_weights = np.array([])
    divide_weights = np.array([])

    def __init__(self, size: int, depth: int, random_seed: int):
        """
        Init layer

        @param: size - size of layer
        """
        np.random.seed(random_seed)
        random.seed(random_seed)
        self.add_weights = np.random.rand(depth, size, size)
        self.subtract_weights = np.random.rand(depth, size, size)
        self.multiply_weights = np.random.rand(depth, size, size)
        self.divide_weights = np.random.rand(depth, size, size)
        self.size = size
        self.depth = depth