import pybullet as p
import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = c.amplitude * numpy.sin(c.frequency * numpy.linspace(0, 2 * numpy.pi, c.simulation_length) + c.phaseOffset)
    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        