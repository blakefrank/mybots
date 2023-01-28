import numpy as np
from solution import SOLUTION
import constants as c
import copy

class HILL_CLIMBER:
    def __init__(self) -> None:
        self.parent = SOLUTION()
        self.weights = np.random.rand(3, 2)
        print(self.weights)
    def evolve(self):
        self.parent.evaluate()
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.evaluate()
        exit()
        self.Select()
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
    def Mutate(self):
        self.child.Mutate()
    def Select(self):
        pass
