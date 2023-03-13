This is my final project, which is based on the Ludobots subreddit. I utilized the hillclimber algorithm developed on r/ludobots and the parallel hillclimber to conduct an evolutionary experiment.

Starting from the conclusion of the Ludobots development, I created a method to generate non-overlapping random bodies using the map class. You can observe this in action by downloading the repository and running map.py to produce a pyrosim or pybullet compatible body map to initiate evolution. This process was complex to develop. Additionally, two algorithms were developed to add and remove blocks in a pybullet-compatible way, ensuring that these bodies remain compatible even after a mutation.

For this experiment, I hypothesized that adding or removing blocks for each generation as a mutation is a more effective form of evolution than solely generating a new brain randomly, resulting in better (fitter) creatures. Fitness was simply defined as the ability to walk quickly, mainly into the screen and away from the user to the left.

To test this, the control group is a simulation of robots that generate a random brain for each successive generation, evolving based on the hillclimber algorithm.

The experimental groups consist of two separate groups, one with an 80% chance of adding a new link after each generation and the other with a 20% chance. Regardless, a link will either be added or removed after each generation, and these numbers control the probabilities. Here are some diagrams to demonstrate how different processses in this experiment work. 

Starting high up, the search.py file runs the evolution of 10 parallel hill climbers in succession. 

![Assignment 8 -1](https://user-images.githubusercontent.com/86979153/224610453-9d058c7b-adb7-4313-bef5-b6658bb6a9d5.jpg)
