<h1 align="center"><b>Videos</b></h1>

[2 min video](https://youtu.be/xcZ4Imb1-G8) (with gif to start)

[gif link](https://imgur.com/8SAZxBe)

**Quick note:** I attempted the scientific option, and I managed to acheive 51,000 simulations as well as test my hypothesis. This took an incredible amount of time, and I hope that my grade reflects the huge amount of effort I put into this project. I also hope you enjoy and appreciate the video and the experiment I did. Thank you!


<h1 align="center"><b>Introduction</b></h1>

This is my final project based on the Ludobots subreddit, where I conducted an evolutionary experiment using the hillclimber algorithm developed on r/ludobots and the parallel hillclimber.

After the Ludobots development, I developed a method to generate non-overlapping random bodies using the map class. You can observe this process by downloading the repository and running map.py to produce a pyrosim or pybullet compatible body map to initiate evolution. Additionally, I created two algorithms to add and remove blocks in a pybullet-compatible way, ensuring that these bodies remain compatible after a mutation. The development of this process was complex.

To actually run my code, download the repo and run search.py with the constants that you desire. Note that any one of my experiments can be recreated by choosing the correct constants that align with the titles of the graphs in the results section. (The seed must be the same as well.)

<h2 align="left"><b>Hypothesis</b></h1>
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

![PHC diagrams ](https://user-images.githubusercontent.com/86979153/224931047-8baecba8-0a9e-4ff7-af1b-731f2735cd3b.jpg)


To summarize, search.py runs 10 instances of the Parallel Hillclimber. Each PHC has a specific number of hillclimbers that evolve based on the hillclimber algorithm. This algorithm generates a child and compares its fitness with the parent, replacing the parent if a beneficial mutation occurred. The map class controls the body of each individual hillclimber, and the mutations. I made sure that every sinlge population is seeded differently. The simple solution for this is to include a random.seed() as the first line run in the code, and the rest will be taken care of through the pseudorandom process that moves a pointer through a list of random numbers.

Also, here is an illustration of how a brain might work. Every sensor neuron is connected with some activation to every motor neuron with no hidden layers of any kind. 

![Note Mar 13, 2023-1](https://user-images.githubusercontent.com/86979153/224905255-8880d459-7c1f-41c1-b34c-b94e0d707282.jpg)

Finally, I do not want to go down the rabbit hole of trying to explain exactly how the MAP class works and the removing of links (and joints) as well as adding them. To see this in action, simply download the repository and run the MAP class as a standalone file, which will allow you to mess around with some of the functions that I wrote. 

<h1 align="center"><b>Methods</b></h1>

I hypothesized that the experimental groups with additive and subractive mutations would outperform the control group, consistently. Here is a diagram that illustrates the three different groups and the difference between them. 

![Page1-2](https://user-images.githubusercontent.com/86979153/224908981-e1233245-f209-491f-8254-5d490b148cf4.jpg)
<h1 align="center"><b>Graphs and Results</b></h1>

How many simulations am I trying to do? Well, we want approximately 17,000 simulations per group. This should work out to 10 PHCs, with population size of 20 and 85 generations. 3 Runs of this gets 51,000 simulations. 20 * 85 * 10 * 3 = 51,000. 

These graphs show the best robot from each generation of each parallel hillclimber with a population size of 20. (Each data point, thus, represents the best of 20 robots). 

Starting with the control group: 

![control](https://user-images.githubusercontent.com/86979153/224901843-d7479887-3ac6-4109-833c-9b9716e9d900.png)

This group's only mutation is re-randomizing the brain (motor and sensor neurons) for each parent's reproduction. 

Experimental group #1 with adding links favored at (80%): 

![addingfavored](https://user-images.githubusercontent.com/86979153/224905349-588b265c-3f97-44c0-af90-60450ea416c4.png)

Experimental group #2 with removing links favored at (80%): 

![remove](https://user-images.githubusercontent.com/86979153/224905436-87450e79-6864-4823-9dcd-82446d16bfc5.png)

Each group ran 17,000 simulations for a total of 50,000 simulations. Each group took approximately 2 hours to run, and failed attempts added many extra frustrating hours. Random "1 in a million" errors occured occasionally. (Errors that occur randomly at a random point in the 2 hour run time and force me to re-run it from scratch.) But alas, we got to 51,000!

<h1 align="center"><b>Discussion</b></h1>

Experimental group #2, which had an 80% chance of removing a link after each generation, was found to be the best performing group. This was surprising as it was initially thought that continuously removing links could potentially hinder the robots' locomotive abilities. While fewer good subtractive mutations occured compared to the control group and experimental group #1, the mutations that did occur were significantly better. As a result, the robot from experimental group #2 (subtractive) was able to walk 25 positions into the screen and would have continued if given more time. Despite starting with 8 to 12 links from the MAP class, the final and best robot contained only 3 links!

The study suggests that complicated mutations and bodies are not always better. The final robot from experimental group #2 simply moved across the screen with a snake-like gallop using only 3 blocks, each containing a sensor neuron. It is remarkable that despite the complexity of the work and algorithms involved, the final robot was able to achieve its impressive performance with such a simple structure.

I did not have time to dive deeper into the individual evolutions of each PHC, as there are hundreds of them, and I cannot at the moment modify my code with little effort to capture all of the simulations. This would take a serious pickling operation on the earlier generations which would require me to re-code entire chunks of the project. I already spent an entire day monitoring my computer and trying to finish the 51000 simulations. If I had more time, I would definitely add more capabilities to my code, such that I could save and analyze the earlier generations and actually visualize individual mutations that were beneficial.

At first glance, however, the charts are very descriptive of the evolutionary process for each mutation and even the control group. Adding blocks resulted in faster and slightly beneficial mutations. Removing blocks resulted in rarer but hugely beneficial mutations. 

<h1 align="center"><b>Conclusion</b></h1>
In this experiment, my goal was to isolate the most beneficial mutation between adding and removing links, if there was one. The experiment was successful, and I found that removing links was the more beneficial mutation. If I had more time, I would conduct further experiments specifically focused on the link-removing mutation, running hundreds of thousands of simulations to determine its true benefits. To accomplish this, I would change the seed to a different sequence of random numbers to ensure the results are not influenced by the initial seed, or simply random. Based on the large number of simulations conducted in this experiment, it is highly unlikely that the results are due to chance alone. However, to further strengthen the findings, it would be interesting to conduct similar experiments with different evolutionary algorithms that do not immediately discard a poorly performing child. These algorithms could evaluate a few generations down the line to ensure that the child's mutation is beneficial in the long run. This would help to further validate the findings of this experiment and provide additional insights into the benefits of adding or removing links in the evolutionary process.
