import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
length = 1
width = 1
height = 1


class SOLUTION:
    def __init__(self) -> None:
        self.weights = np.random.rand(3, 2)
        self.weights = (self.weights * 2) - 1
        
    def Create_World(self): 
        pyrosim.Start_NeuralNetwork("brain.nndf")
        sensor_neurons = [0, 1, 2]
        motor_neurons = [0, 1]
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

		# Motor neurons
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        for currentRow in sensor_neurons:
            for currentColumn in motor_neurons:
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + 3 , weight = self.weights[currentRow][currentColumn] )
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_SDF("box.sdf")
        pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[length, width, height])
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0, 1] , size=[1, 1, 1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-0.5,0, .5])
        pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0, -.5] , size=[1,1,1])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position= [.5, 0, .5])
        pyrosim.Send_Cube(name="FrontLeg", pos=[.5,0, -.5] , size=[1,1,1])
        pyrosim.End()

    def Create_Brain(self):
        self.Create_Body()
        self.Create_World()

    def evaluate(self):
        self.Create_Brain()
        os.system("python3 simulate.py")
        fitnessFile = open("fitness.txt", "r")
        fitnessValue = float(fitnessFile.read())
        self.fitness = fitnessValue
        fitnessFile.close()
    
    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1



