import pyrosim.pyrosim as pyrosim
import random
length = 1
width = 1
height = 1

def Generate_Body():
    pyrosim.Start_SDF("box.sdf")
    pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[length, width, height])
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0,0, 1] , size=[1, 1, 1])
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-0.5,0, .5])
    pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0, -.5] , size=[1,1,1])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position= [.5, 0, .5])
    pyrosim.Send_Cube(name="FrontLeg", pos=[.5,0, -.5] , size=[1,1,1])
    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    sensor_neurons = [0, 1, 2]
    motor_neurons = [3, 4]
    for i in sensor_neurons:
        pyrosim.Send_Sensor_Neuron(name = i , linkName = "Torso")
        for j in motor_neurons:
            pyrosim.Send_Motor_Neuron( name = j , jointName = "Torso_BackLeg") 
            weight = random.uniform(-1,1)
            pyrosim.Send_Synapse( sourceNeuronName = i , targetNeuronName = j , weight = weight )
    pyrosim.End()


def Create_World():
    Generate_Body()
    Generate_Brain()

Create_World()
