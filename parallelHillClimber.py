import numpy as np
from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
	def __init__(self) -> None:
		os.system("rm brain*.nndf")
		os.system("rm fitness*.txt")
		self.parents = {}
		self.nextAvailableID = 0
		for populationID in range(c.populationSize):
			self.parents[populationID] = SOLUTION(self.nextAvailableID, populationID)
			self.nextAvailableID += 1
		# self.weights = np.random.rand(3, 2)

	def evolve(self):
		self.Evaluate(self.parents)
		
		# self.parent.evaluate("GUI")
		for currentGeneration in range(c.numberOfGenerations):
			self.Evolve_For_One_Generation()
		# self.SHOW_BEST()
		

	def Evolve_For_One_Generation(self):
		self.Spawn()
		self.Mutate() 
		self.Evaluate(self.children)
		self.Print()
		self.Select()

	def Spawn(self):
		self.children = dict()
		for key in self.parents:
			self.children[key] = copy.deepcopy(self.parents[key])
			self.children[key].Set_ID(self.nextAvailableID)
			self.nextAvailableID = self.nextAvailableID + 1

	def Mutate(self):
		for key in self.children:
			self.children[key].Mutate()

	def Select(self):
		for key in self.parents:
			if self.parents[key].fitness > self.children[key].fitness:
				self.parents[key] = self.children[key]

	def Print(self):
		print("")
		print("")
		for key in self.parents:
			print("Parent " + str(key) + ": " + str(self.parents[key].fitness) + " Child: " + str(self.children[key].fitness))
		print("")
	def Show_Best(self):
		bestKey = 0
		for key in self.parents:
			if self.parents[key].fitness < self.parents[bestKey].fitness:
				bestKey = key
		self.parents[bestKey].Start_Simulation("GUI")
		self.parents[bestKey].Wait_For_Simulation_To_End("GUI")
		print("-------------------------------BEST FITNESS-------------------------------")
		print(self.parents[bestKey].fitness)



	def Evaluate(self, solutions):
		for i in solutions:
			solutions[i].Start_Simulation("DIRECT")
		for i in solutions:
			solutions[i].Wait_For_Simulation_To_End("DIRECT")
