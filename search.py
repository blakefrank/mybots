
import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
# for i in range(5):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")
os.system("rm body*.urdf")
phc = PARALLEL_HILL_CLIMBER()
phc.evolve()
phc.Show_Best()


