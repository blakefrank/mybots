import numpy as np
from solution import SOLUTION
import constants as c
import copy
import os
import random
from map import MAP
import matplotlib.pyplot as plt
import shutil

class PARALLEL_HILL_CLIMBER:
	def __init__(self, number) -> None:
		os.system("rm brain*.nndf")
		os.system("rm fitness*.txt")
		self.number = number
		self.parents = {}
		self.nextAvailableID = 0
		self.graph = np.empty((c.populationSize, c.numberOfGenerations))
		self.currgen = 0
		for populationID in range(c.populationSize):
			numlinks=random.randint(8,12)
			new_map = MAP(numlinks)
			self.parents[populationID] = SOLUTION(self.nextAvailableID, populationID, numlinks=numlinks, map_in=new_map)
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
		# print("")
		# print("")
		for key in self.parents:
			# print("Parent " + str(key) + ": " + str(self.parents[key].fitness) + " Child: " + str(self.children[key].fitness))
			self.graph[key][self.currgen] = -1*self.parents[key].fitness
		# print("")
		self.currgen+=1
	def Show_Best(self):

		
		bestKey = 0
		for key in self.parents:
			print(self.parents[key].fitness)
			if self.parents[key].fitness < self.parents[bestKey].fitness:
				bestKey = key
		print("-------------------------------BEST FITNESS-------------------------------")
		print(self.parents[bestKey].fitness)
		self.parents[bestKey].Start_Simulation("GUI")
		self.parents[bestKey].Wait_For_Simulation_To_End("GUI")
		
		



	def Evaluate(self, solutions):
		for i in solutions:
			solutions[i].Start_Simulation("DIRECT")
		for i in solutions:
			solutions[i].Wait_For_Simulation_To_End("DIRECT")
		
	def get_avg_row(self):
		# Calculate the average fitness over generations
		average_fitness = np.mean(self.graph, axis=0)

		return average_fitness

	def find_best_fitness_value(self):
		self.highest_row_index = np.argmax(self.graph, axis=0)
		best_body_file = f'body{self.highest_row_index}.urdf'
		best_body_dir = f'phc{self.number}'

		# Create the directory if it doesn't exist
		if not os.path.exists(best_body_dir):
			os.makedirs(best_body_dir)

		# Copy all body files to the directory
		for i, parent in enumerate(self.parents):
			body_file = f'body{i}.urdf'
			shutil.copyfile(body_file, os.path.join(best_body_dir, body_file))

		# Return the highest fitness value
		return np.amax(self.graph)