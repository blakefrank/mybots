import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR
import constants as c
import os
class ROBOT:

    def __init__(self):

        pass

    def Save_Start_Tag(self,f):

        f.write('<robot name="robot">\n')

    def Save_End_Tag(self,f):

        f.write("</robot>")
