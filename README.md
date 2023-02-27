This is Assignment 8, which involves the creation of randomized body plans and their evolution through successive generations, achieved by making changes to the brain and body. To facilitate this task, we will make reference to the documentation from Assignment 7. To learn about the operation of Assignment 7 and the process of body generation using the MAP class, please refer to this link. [see here](https://github.com/blakefrank/mybots/tree/3d-morphologies)

See the diagram below for the process of how functions call eachother.
![Assignment 8 ](https://user-images.githubusercontent.com/86979153/221684765-38b05540-36fa-43f0-b8ea-ad2a2c1eb4f8.jpg)


The MAP class is tailored to the population size, which in this case is 5. To enhance its capabilities, a new method called "remove_edge_block(self)" was added to the MAP class. This method utilizes string comparisons, as well as the properties of joints and links, to randomly select and remove an edge joint and link. An edge link is defined as one that does not have a joint with that link as its parent.

Subsequently, the "remove_edge_block(self)" function was integrated into the "Mutate()" function of "solution.py". This modification allows for a 50% chance of removing a link and joint and a 50% chance of adding a new link and joint, using the existing function in MAP.

Once the process is complete, each lineage is plotted and the best offspring is presented in the simulation. Here is an example of what a fitness curve might look like with Population = 5 and Generations = 10: 

<img width="578" alt="Screen Shot 2023-02-27 at 3 03 20 PM" src="https://user-images.githubusercontent.com/86979153/221685180-0efafb9a-a6ab-488e-b323-e80ca989e179.png">

Right now, the code is still not perfect. There is an issue sometimes with removing and adding links. Currently, when both capabilities (adding and removing) are both activated, the code will occasionally run into errors in brain generation. I am still trying to get to the bottom of this. The mutations generally work well and generate a fit robot!
