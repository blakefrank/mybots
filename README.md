This is Assignment 8, which involves the creation of randomized body plans and their evolution through successive generations, achieved by making changes to the brain and body. To facilitate this task, we will make reference to the documentation from Assignment 7. To learn about the operation of Assignment 7 and the process of body generation using the MAP class, please refer to this link. [see here](https://github.com/blakefrank/mybots/tree/3d-morphologies)

See the diagram below for the process of how functions call eachother.
![Assignment 8 ](https://user-images.githubusercontent.com/86979153/221661105-45452b49-f227-49b9-9b36-7f5d7f86592d.jpg)

The MAP class is tailored to the population size, which in this case is 5. To enhance its capabilities, a new method called "remove_edge_block(self)" was added to the MAP class. This method utilizes string comparisons, as well as the properties of joints and links, to randomly select and remove an edge joint and link. An edge link is defined as one that does not have a joint with that link as its parent.

Subsequently, the "remove_edge_block(self)" function was integrated into the "Mutate()" function of "solution.py". This modification allows for a 50% chance of removing a link and joint and a 50% chance of adding a new link and joint, using the existing function in MAP.

Once the process is complete, each lineage is plotted and the best offspring is presented in the simulation.
