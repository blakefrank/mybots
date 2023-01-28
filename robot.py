import pybullet as p
import pyrosim
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self, physicsClient):
        self.physicsClient = physicsClient
        self.motors = {}
        self.sensors = {}
        self.initialpos = [0, 1, 0.5]
        self.robotId = p.loadURDF("body.urdf", self.initialpos)
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain.nndf")
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
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName.encode('utf-8')].Set_Value(desiredAngle)
                # print("----------current desired angle-------------")
                # print(desiredAngle)
                # print("----------current neuron name-------------")
                # print(neuronName)
                # print("----------current joint name-------------")
                # print(jointName)
        # for motor in self.motors.values():
        #     motor.Set_Value(i)
    def Think(self):
        self.nn.Print()
        self.nn.Update()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        print(xCoordinateOfLinkZero)
        exit()




            
    

        
