import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time
length = 1
width = 1
height = 1


class SOLUTION:
	def __init__(self, nextAvailableID, populationID):
		self.myID = nextAvailableID
		self.populationID = populationID
		self.Create_Body()

	def Create_Brain(self): 
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		neuronName = 0

		for i in range(self.numLinks):

			if self.sensorLocs[i] == 1:
				linkName = "Link" + str(i+1)
				pyrosim.Send_Sensor_Neuron(name = neuronName , linkName = linkName)

				neuronName += 1
		
		self.numSensorNeurons = neuronName

		for i in range(1,self.numLinks):
			jointName = "Link" + str(i) + "_Link" + str(i+1)
			pyrosim.Send_Motor_Neuron( name = neuronName , jointName = jointName)
			neuronName += 1
		self.weights = np.random.rand(self.numSensorNeurons, self.numLinks-1)*2 - 1


		for currentRow in range(self.numSensorNeurons):
			for currentColumn in range(self.numLinks-1):
				pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+self.numSensorNeurons , weight = self.weights[currentRow][currentColumn] )

		pyrosim.End()

	def Create_Body(self):
		head_length = random.random() + 0.1
		head_width = random.random() + 0.3
		head_height = random.random() + 0.15

		pyrosim.Start_URDF("body" + str(self.populationID) + ".urdf")

		# Length of body
		self.numLinks = random.randint(4,12)
		self.sensorLocs = np.random.randint(2, size=self.numLinks)

		material = "Green" if self.sensorLocs[0] == 1 else "Blue"

		# Head
		pyrosim.Send_Cube(name="Link1", pos=[0,0,1] , size=[head_length,head_width,head_height], material = material, rgba = self.Get_rgba(material))

		# Link 1
		link_length = random.random() + 0.1
		link_width = random.random() + 0.3
		link_height = random.random() + 0.15
		material = "Green" if self.sensorLocs[1] == 1 else "Blue"
		pyrosim.Send_Joint( name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [head_length/2,0,1], jointAxis = "0 1 0")
		pyrosim.Send_Cube(name= "Link2", pos=[link_length/2,0,0] , size=[link_length,link_width,link_height], material = material, rgba = self.Get_rgba(material))
		
		prevLinkLength = link_length

		# Additional links
		for i in range(2,self.numLinks):
			link_length = random.random() + 0.1
			link_width = random.random() + 0.3
			link_height = random.random() + 0.15

			jointName = "Link" + str(i) + "_Link" + str(i+1)
			parentName = "Link" + str(i)
			childName = "Link" + str(i+1)

			pyrosim.Send_Joint( name = jointName , parent= parentName , child = childName , type = "revolute", position = [prevLinkLength,0,0], jointAxis = "0 1 0")
			material = "Green" if self.sensorLocs[i] == 1 else "Blue"
			pyrosim.Send_Cube(name= childName, pos=[link_length/2,0,0] , size=[link_length,link_width,link_height], material = material, rgba = self.Get_rgba(material))
			prevLinkLength = link_length

		pyrosim.End()


	def Create_World(self):
		pyrosim.Start_SDF("world.sdf")
		pyrosim.Send_Cube(name="Box", pos=[-3,3,0.5] , size=[1,1,1])
		pyrosim.End()
	
	def evaluate(self, directOrGUI):
		pass
	
	def Start_Simulation(self, directOrGUI):
		self.Create_World()
		self.Create_Body()
		# os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " " + str(self.populationID) + " 2&>1 &")
		os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " " + str(self.populationID) + " &")
		
	def Wait_For_Simulation_To_End(self, directOrGUI):
		while not os.path.exists("fitness" + str(self.myID) + ".txt"):
			time.sleep(1)
		fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
		fitnessValue = float(fitnessFile.read())
		self.fitness = fitnessValue
		fitnessFile.close()
		os.system("rm fitness" + str(self.myID) + ".txt")

	def Mutate(self):
		randomRow = random.randint(0,self.numSensorNeurons-1)
		randomColumn = random.randint(0,self.numLinks-2)
		self.weights[randomRow, randomColumn] = random.random() * 2 - 1

	def Set_ID(self, id):
		self.myID = id

	def Get_rgba(self, material):
		if material == "Blue":
			return "0 0 1.0 1.0"
		elif material == "Green":
			return "0 1.0 0 1.0"
		else:
			return "0 1.0 1.0 1.0"

