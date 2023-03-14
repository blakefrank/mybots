<h1 align="center"><b>Introduction</b></h1>

This is my final project based on the Ludobots subreddit, where I conducted an evolutionary experiment using the hillclimber algorithm developed on r/ludobots and the parallel hillclimber.

After the Ludobots development, I developed a method to generate non-overlapping random bodies using the map class. You can observe this process by downloading the repository and running map.py to produce a pyrosim or pybullet compatible body map to initiate evolution. Additionally, I created two algorithms to add and remove blocks in a pybullet-compatible way, ensuring that these bodies remain compatible after a mutation. The development of this process was complex.

My hypothesis for this experiment was that adding or removing blocks as a mutation for each generation is a more effective form of evolution than generating a new brain randomly, resulting in fitter creatures. In this case, fitness was defined as the ability to walk quickly, mainly into the screen and away from the user to the left.

This hypothesis is general and speculates that a mutation such as adding or removing links will be beneficial to the creature over time, using the hillclimber algorithm. This algorithm simply replaces the parent with a child if the child outperforms the parent.

To test this, the control group comprised a simulation of robots that generated a random brain for each successive generation, evolving based on the hillclimber algorithm.

The experimental groups consisted of two separate groups, one with an 80% chance of adding a new link after each generation and the other with a 20% chance. Regardless, a link would be added or removed after each generation, and these probabilities were controlled. Diagrams were provided to demonstrate the different processes in this experiment.

Starting with the search.py file, the evolution of ten parallel hill climbers occurred successively.

Here is a higher up overview of what is going on

![Assignment 8 -1](https://user-images.githubusercontent.com/86979153/224610453-9d058c7b-adb7-4313-bef5-b6658bb6a9d5.jpg)

Going a bit deeper, each PHC is initialized with the MAP class creating random bodies according to the population size. The MAP class instantly creates links and joints to form a body that can be used for evolution. Each robots starts with 8 to 12 links (random amount).


![Page1-1](https://user-images.githubusercontent.com/86979153/224611926-8b60ef86-6d20-47c5-a593-156ac07d03c0.jpg)
![Page2-1](https://user-images.githubusercontent.com/86979153/224611939-7252b450-3541-4e5b-9d07-78c0b76b9290.jpg)

Furthermore, after the creation of each PHC, every member of the population is initialized with the MAP class. Then, the PHC employs parallel hillclimber algorithms, as illustrated below, to facilitate reproduction and mutation.

![Page1-2](https://user-images.githubusercontent.com/86979153/224908981-e1233245-f209-491f-8254-5d490b148cf4.jpg)

To summarize, search.py runs 10 instances of the Parallel Hillclimber. Each PHC has a specific number of hillclimbers that evolve based on the hillclimber algorithm. This algorithm generates a child and compares its fitness with the parent, replacing the parent if a beneficial mutation occurred. The map class controls the body of each individual hillclimber, and the mutations. 

Also, here is an illustration of how a brain might work. Every sensor neuron is connected with some activation to every motor neuron with no hidden layers of any kind. 

![Note Mar 13, 2023-1](https://user-images.githubusercontent.com/86979153/224905255-8880d459-7c1f-41c1-b34c-b94e0d707282.jpg)


<h1 align="center"><b>Methods</b></h1>

I hypothesized that the Experimental groups with additive and subractive mutations would outperform the control group, consistently. Here is a diagram that illustrates the three different groups and the difference between them. 

![Note Mar 13, 2023](https://user-images.githubusercontent.com/86979153/224774918-bc7aedc4-20c9-4eb4-b881-c29bd05af554.jpg)
<h1 align="center"><b>Graphs and Results</b></h1>

How many simulations am I trying to do? Well, we want approximately 17,000 simulations per group. This should work out to 10 PHCs, with population size of 20 and 85 generations. 3 Runs of this gets 51,000 simulations. 20 * 85 * 10 * 3 = 51,000. 

Starting with the control group: 

![control](https://user-images.githubusercontent.com/86979153/224901843-d7479887-3ac6-4109-833c-9b9716e9d900.png)

This group's only mutation is re-randomizing the brain (motor and sensor neurons) for each parent's reproduction. 

Experimental group #1 with adding links favored at (80%): 

![addingfavored](https://user-images.githubusercontent.com/86979153/224905349-588b265c-3f97-44c0-af90-60450ea416c4.png)

Experimental group #2 with removing links favored at (80%): 

![remove](https://user-images.githubusercontent.com/86979153/224905436-87450e79-6864-4823-9dcd-82446d16bfc5.png)

Each group ran 17,000 simulations for a total of 50,000 simulations. Each group took approximately 2 hours to run, and failed attempts added many extra frustrating hours. Random "1 in a million" errors occured occasionally. (Errors that occur randomly at a random point in the 2 hour run time and force me to re-run it from scratch.) But alas, we got to 51,000!

<h1 align="center"><b>Discussion</b></h1>

Experimental group #2, which had an 80% chance of removing a link after each generation, was found to be the best performing group. This was surprising as it was initially thought that continuously removing links could potentially hinder the robots' locomotive abilities. While fewer good mutations were created compared to the control group and experimental group #1, the mutations that did occur were significantly better. As a result, the robot from experimental group #2 was able to walk 25 positions into the screen and would have continued if given more time. Despite starting with 8 to 12 links from the MAP class, the final and best robot contained only 3 links!

The study suggests that complicated mutations and bodies are not always better. The final robot from experimental group #2 simply moved across the screen with a snake-like gallop using only 3 blocks, each containing a sensor neuron. It is remarkable that despite the complexity of the work and algorithms involved, the final robot was able to achieve its impressive performance with such a simple structure.
