This is my final project based on the Ludobots subreddit, where I conducted an evolutionary experiment using the hillclimber algorithm developed on r/ludobots and the parallel hillclimber.

After the Ludobots development, I developed a method to generate non-overlapping random bodies using the map class. You can observe this process by downloading the repository and running map.py to produce a pyrosim or pybullet compatible body map to initiate evolution. Additionally, I created two algorithms to add and remove blocks in a pybullet-compatible way, ensuring that these bodies remain compatible after a mutation. The development of this process was complex.

My hypothesis for this experiment was that adding or removing blocks as a mutation for each generation is a more effective form of evolution than generating a new brain randomly, resulting in fitter creatures. In this case, fitness was defined as the ability to walk quickly, mainly into the screen and away from the user to the left.

To test this, the control group comprised a simulation of robots that generated a random brain for each successive generation, evolving based on the hillclimber algorithm.

The experimental groups consisted of two separate groups, one with an 80% chance of adding a new link after each generation and the other with a 20% chance. Regardless, a link would be added or removed after each generation, and these probabilities were controlled. Diagrams were provided to demonstrate the different processes in this experiment.

Starting with the search.py file, the evolution of ten parallel hill climbers occurred successively.

Here is a higher up overview of what is going on

![Assignment 8 -1](https://user-images.githubusercontent.com/86979153/224610453-9d058c7b-adb7-4313-bef5-b6658bb6a9d5.jpg)

Going a bit deeper, each PHC is initialized with the MAP class creating random bodies according to the population size. The MAP class instantly creates links and joints to form a body that can be used for evolution.


![Page1-1](https://user-images.githubusercontent.com/86979153/224611926-8b60ef86-6d20-47c5-a593-156ac07d03c0.jpg)
![Page2-1](https://user-images.githubusercontent.com/86979153/224611939-7252b450-3541-4e5b-9d07-78c0b76b9290.jpg)

Going even deeper, after each PHC is created, each member of the population is initialized with the MAP class. The PHC then uses literally parrallel hillclimber algorithms to facilitate reproduction and mutation, as shown below.
![PHC diagrams ](https://user-images.githubusercontent.com/86979153/224771055-0bc3d152-52b4-4adf-b870-d5d39aaa82ef.jpg)


