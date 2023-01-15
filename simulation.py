from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim
import constants as c
import time
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
            self.robot.sense()
            time.sleep(1/60)
            print(i)
            # p.stepSimulation()
            # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex = robotId,
            #     jointName = b"Torso_BackLeg",
            #     controlMode = p.POSITION_CONTROL,
            #     targetPosition = targetAngles[i],
            #     maxForce = 500
            # )
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex = robotId,
            #     jointName = b"Torso_FrontLeg",
            #     controlMode = p.POSITION_CONTROL,
            #     targetPosition = targetAngles1[i],
            #     maxForce = 500
            # )
            # print(backLegSensorValues[i])
    def __del__(self):
        p.disconnect()
        
          
