import pybullet as p
import numpy
import constants as c
import pyrosim.pyrosim
class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = c.amplitude * numpy.sin(c.frequency * numpy.linspace(0, 2 * numpy.pi, c.simulation_length) + c.phaseOffset)
        print("------------Three Empy Vectors--------------")
        print(self.values)
    def Get_Value(self):
        self.values = p.getJointState(self.robotId, self.linkName)