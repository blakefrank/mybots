import pybullet as p
import pyrosim
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR

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
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            print(linkName)
            self.sensors[linkName] = SENSOR(linkName)
    def Sense(self, t):
        for sensor in self.sensors.values():
            sensor.Get_Value(t)
    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName, self)
    def Act(self, i):
        for motor in self.motors.values():
            motor.Set_Value(i)


            
    

        
