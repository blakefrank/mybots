import numpy as np
from solution import SOLUTION
import constants as c
import copy

class HILL_CLIMBER:
    def __init__(self) -> None:
        self.parent = SOLUTION()
        self.weights = np.random.rand(3, 2)
    def evolve(self):
        self.parent.evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        self.SHOW_BEST()
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.evaluate("DIRECT")
        self.Print()
        self.Select()
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
    def Mutate(self):
        self.child.Mutate()
    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child
    def Print(self):
        print(self.parent.fitness, end=' ')
        print(self.child.fitness)
    def SHOW_BEST(self):
        self.parent.evaluate("GUI")
