import pybullet as p
import pyrosim
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c
import os

class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.motors = {}
        self.sensors = {}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        os.system("rm brain" + str(solutionID) + ".nndf")
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    def Sense(self, t):
        for sensor in self.sensors.values():
            sensor.Get_Value(t)
    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName, self)
    def Act(self, i):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)*c.motorJointRange
                self.motors[jointName.encode('utf-8')].Set_Value(desiredAngle)
    def Think(self):
        #self.nn.Print()
        self.nn.Update()

    def Get_Fitness(self):
        position = p.getBasePositionAndOrientation(self.robotId)[0]
        height = -1*position[2]
        with open("tmp" + str(self.solutionID) + ".txt", "w") as file:
            file.write(str(height))
            os.system("mv tmp" + str(self.solutionID) + ".txt fitness" + str(self.solutionID) + ".txt")




            
    

        
