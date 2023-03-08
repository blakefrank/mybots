import os
import numpy as np
import matplotlib.pyplot as plt
import constants as c
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import shutil
import time

import pickle


# Load the variable from the file in another program
with open('my_variable.pickle', 'rb') as f:
    my_variable = pickle.load(f)

my_variable.Show_Best()