from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
import time
import numpy

class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.physicsClient = p.connect(p.GUI)
        self.robot = ROBOT(self.physicsClient)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)  
        p.loadSDF("world.sdf")
        self.planeId = p.loadURDF("plane.urdf")

    def Run(self):
        for i in range(c.simulation_length):
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            p.stepSimulation()
            time.sleep(1/60)
            #print(i)

    def Save_Values(self):
        for linkName, sensor in self.robot.sensors.items():
            numpy.save("data/{}SensorValues.npy".format(linkName), sensor.values)
        for jointName, motor in self.robot.motors.items():
            numpy.save("data/{}MotorValues.npy".format(jointName), motor.motorValues)

    def __del__(self):
        p.disconnect()