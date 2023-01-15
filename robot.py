import pybullet as p
import pyrosim
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR

class ROBOT:
    def __init__(self, physicsClient):
        self.physicsClient = physicsClient
        self.motors = {}
        self.initialpos = [0, 1, 0.5]
        self.robotId = p.loadURDF("body.urdf", self.initialpos)
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            print(linkName)
            self.sensors[linkName] = SENSOR(linkName)
    def Sense(self):
        

            
    

        
