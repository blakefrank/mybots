import numpy as np
from solution import SOLUTION

class HILL_CLIMBER:
    def __init__(self) -> None:
        self.parent = SOLUTION()
        self.weights = np.random.rand(3, 2)
        print(self.weights)
    def evolve(self):
        self.parent.evaluate()