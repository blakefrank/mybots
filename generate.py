import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("box.sdf")
length = 1
width = 1
height = 1
start = [0,0,0.5]
newpos = start
for x in range(5):
    for y in range(5):
        for i in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x,y,(10-pow(9, i+1)*pow(10,-i)) + 0.01*i-0.4] , size=[length*pow(0.9,i),width*pow(0.9,i),height*pow(0.9,i)])
pyrosim.End()