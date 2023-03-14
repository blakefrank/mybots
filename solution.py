import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np
import random
import time
import os
from map import MAP
import copy


class SOLUTION:
	def __init__(self, nextAvailableID, populationID, numlinks, map_in):
		self.myID = nextAvailableID
		self.populationID = populationID
		self.numLinks = numlinks
		self.map = map_in
		while True:
			self.sensorLocs = np.random.randint(2, size=self.numLinks)
			if np.count_nonzero(self.sensorLocs) > 1:
				break
		self.Create_Body()
		self.weights_initialized = False
		
		
		

	def Create_Brain(self): 
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		neuronName = 0
		links = self.map.list_links
		joints = self.map.list_joints

		for i in range(len(self.map.list_links)):
			if self.sensorLocs[i] == 1:
				linkName = links[i].name
				pyrosim.Send_Sensor_Neuron(name = neuronName , linkName = linkName)
				neuronName +=1 
		
		self.numSensorNeurons = neuronName

		for i in range(len(self.map.list_joints)):
			jointName = joints[i].name
			pyrosim.Send_Motor_Neuron( name = neuronName , jointName = jointName)
			neuronName += 1

		if self.weights_initialized == False:
			self.weights = np.random.rand(self.numSensorNeurons, self.numLinks-1)*2 - 1


		for currentRow in range(self.numSensorNeurons):
			for currentColumn in range(self.numLinks-1):
				pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+self.numSensorNeurons , weight = self.weights[currentRow][currentColumn] )

		self.weights_initialized= True
		pyrosim.End()

	def Create_Body(self):
		links = self.map.list_links
		joints = self.map.list_joints

		pyrosim.Start_URDF("body" + str(self.populationID) + ".urdf")

		# Length of body
		
		

		material = "Green" if self.sensorLocs[0] == 1 else "Blue"

		# Head
		pyrosim.Send_Cube(name=links[0].name, pos=links[0].abs , size=[1,1,1], material = material, rgba = self.Get_rgba(material))

		# Additional links
		for i in range(len(joints)):
			curr_joint = joints[i]
			jointName = curr_joint.name
			parentName = curr_joint.parent.name
			childName = curr_joint.child.name
			childPos = curr_joint.child.rel

			if type(curr_joint.rel) == type(None):
				jointPos = curr_joint.abs
			else:
				jointPos = curr_joint.rel 

			jointAxis = curr_joint.axis

			pyrosim.Send_Joint( name = jointName , parent= parentName , child = childName , type = "revolute", position = jointPos, jointAxis = jointAxis)

			material = "Green" if self.sensorLocs[i] == 1 else "Blue"
			pyrosim.Send_Cube(name= childName, pos=childPos, size=[1,1,1], material = material, rgba = self.Get_rgba(material))

		pyrosim.End()


	def Create_World(self):
		length = 1
		width = 1
		height = 1

		x = 0
		y = 0
		z = height/2

		pyrosim.Start_SDF("world.sdf")

		pyrosim.Send_Cube(name="Box", pos=[-4,4,z] , size=[length,width,height])

		pyrosim.End()
	
	
	def Start_Simulation(self, directOrGUI):
		self.Create_Body()
		self.Create_World()
		self.Create_Brain()

		os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " " + str(self.populationID) + " 2&>1 &")
		# os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " " + str(self.populationID) + " &")
		
	def Wait_For_Simulation_To_End(self, directOrGUI):
		while not os.path.exists("fitness" + str(self.myID) + ".txt"):
			time.sleep(0.02)
		fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
		while True:
			try:
				fitnessValue = float(fitnessFile.read())
				self.fitness = fitnessValue
				fitnessFile.close()
				break
			except:
				continue
		os.system("rm fitness" + str(self.myID) + ".txt")

		


	def Mutate(self):
		randomRow = random.randint(0,self.numSensorNeurons-1)
		randomColumn = random.randint(0,self.numLinks-2)
		self.weights[randomRow, randomColumn] = random.random() * 2 - 1
		random_number = random.random()
		if random_number < c.probtoremove:
			if len(self.map.list_links) > 3:
				# pass
				self.map.remove_edge_block()
				self.map.fix()
				while True:
					self.sensorLocs = np.random.randint(2, size=len(self.map.list_links))
					if np.count_nonzero(self.sensorLocs) > 1:
						break


				# print("--------Link Removed----------")
				# print("--------SensorLocs----------")
				# print(self.sensorLocs)
				# print("--------Numlinks----------")
				# print(len(self.map.list_links))
				self.Create_Body()
			else:
				pass
		else:
			# pass
			while self.map.find_new_joint_and_link() != False:
				pass
			self.map.incr()
			# self.numLinks +=1
			while True:
				self.sensorLocs = np.random.randint(2, size=len(self.map.list_links))
				if np.count_nonzero(self.sensorLocs) > 1:
					break




			# print("--------Link Added----------")
			# print("--------SensorLocs----------")
			# print(self.sensorLocs)
			# print("--------Numlinks----------")
			# print(len(self.map.list_links))
			self.Create_Body()
			
			


		
		self.weights_initialized = False


	def Set_ID(self, id):
		self.myID = id

	def Get_rgba(self, material):
		if material == "Blue":
			return "0 0 1.0 1.0"
		elif material == "Green":
			return "0 1.0 0 1.0"
		else:
			return "0 1.0 1.0 1.0"

