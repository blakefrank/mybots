import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c
class MOTOR:
    def __init__(self, jointName, robot):
        self.jointName = jointName
        self.robot = robot
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseOffset
        # self.Prepare_To_Act()

        
    # def Prepare_To_Act(self):
    #     for jointName in pyrosim.jointNamesToIndices:
    #         if self.jointName == b'Torso_BackLeg':
    #             self.frequency = c.frequency
    #         else:
    #             self.frequency = c.frequency/2
    #         self.motorValues = self.amplitude * numpy.sin(self.frequency * numpy.linspace(0, 2 * numpy.pi, c.simulation_length) + self.offset)


    def Set_Value(self, desiredAngle):
        targetPosition = desiredAngle
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = self.robot.robotId,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetPosition,
        maxForce = 100
    )