import os
import numpy as np
import matplotlib.pyplot as plt
import constants as c
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import shutil
import time
import pickle
import random

np.random.seed(c.randomSeed)
random.seed(c.randomSeed)
max_fitness_value = -np.inf # initialize to negative infinity
max_fitness_phc = None # initialize to None
arr = np.zeros((c.numberOfGenerations, 5))
for i in range(c.number_of_phcs):
    phc = PARALLEL_HILL_CLIMBER(i)
    phc.evolve()
    new_row = phc.get_avg_row()
    arr[:, i] = new_row # Append the new row to the array
    fitness_value = phc.find_best_fitness_value()
    if fitness_value > max_fitness_value:
        max_fitness_value = fitness_value
        max_fitness_phc = phc

    # Plot the new row as a line
    plt.plot(range(c.numberOfGenerations), new_row, label=f'phc {i+1}')

print("------cleaning up body files, waiting 5 sec--------")
os.system("rm body*.urdf")
time.sleep(5)

for i in range(c.populationSize):
    src = f"phc{max_fitness_phc.number}/body{i}.urdf"
    dst = f"body{i}.urdf"
    shutil.copyfile(src, dst)

# Delete all directories starting with "phc"
for dir_name in os.listdir('.'):
    if os.path.isdir(dir_name) and dir_name.startswith('phc'):
        shutil.rmtree(dir_name)

# Set the title and axis labels
plt.title(f'Average Fitness over PHC Generations (Population Size: {c.populationSize}, \nGenerations: {c.numberOfGenerations}, PHCs: {c.number_of_phcs}, Random Seed: {c.randomSeed}), P(remove) = {c.probtoremove})')
plt.xlabel('Generation')
plt.ylabel('Fitness')

# Add a legend to show which line corresponds to which individual
plt.legend()

# Define the filename for saving the plot
filename = f'fitness_plot_pop{c.populationSize}_gen{c.numberOfGenerations}_phcs{c.number_of_phcs}_seed{c.randomSeed}_PR{c.probtoremove}.png'

# Save the plot to the specified filename
plt.savefig(filename)

# Display the plot
plt.show()




# Call Show_Best() on the instance with the highest fitness value

# Define the variable you want to save
my_variable = max_fitness_phc

# Save the variable to a file
with open('my_variable.pickle', 'wb') as f:
    pickle.dump(my_variable, f)

max_fitness_phc.Show_Best()



exit()



