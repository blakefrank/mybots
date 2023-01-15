from simulation import SIMULATION
simulation = SIMULATION()
simulation.Run()


# import pybullet as p
# import time
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import numpy
# import constants as c



# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.setGravity(0,0,-9.8)
# p.loadSDF("world.sdf")
# planeId = p.loadURDF("plane.urdf")
# initial_pos = [0, 1, 0.5]
# robotId = p.loadURDF("body.urdf", initial_pos)

# pyrosim.Prepare_To_Simulate(robotId)

# backLegSensorValues = numpy.zeros(c.simulation_length)
# frontLegSensorValues = numpy.zeros(c.simulation_length)
# backLegMotorAngles = numpy.zeros(c.imulation_length)
# frontLegMotorAngles = numpy.zeros(c.simulation_length)
# # Create the motor command vector

# targetAngles = c.amplitude * numpy.sin(c.frequency * numpy.linspace(0, 2 * numpy.pi, simulation_length) + c.phaseOffset)
# numpy.save("data/targetAngles.npy", targetAngles)


# targetAngles1 = c.amplitude * numpy.sin(c.frequency * numpy.linspace(0, 2 * numpy.pi, simulation_length) + c.phaseOffset1)
# numpy.save("data/targetAngles1.npy", targetAngles1)

# for i in range(simulation_length):
#     time.sleep(1/60)
#     p.stepSimulation()
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = b"Torso_BackLeg",
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = targetAngles[i],
#         maxForce = 500
#     )
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = b"Torso_FrontLeg",
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = targetAngles1[i],
#         maxForce = 500
#     )
#     print(backLegSensorValues[i])

# numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
# numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
# p.disconnect()
