![Page1](https://user-images.githubusercontent.com/86979153/220497788-6b1c6484-cf55-4c19-acce-27e7383ae580.jpg)
![Page2](https://user-images.githubusercontent.com/86979153/220497814-dca0bab5-d950-4bff-9581-ddae9109d0d5.jpg)
<img width="842" alt="Screen Shot 2023-02-21 at 7 34 11 PM" src="https://user-images.githubusercontent.com/86979153/220498078-baafafa7-b00a-4806-9945-9c3ac0f29256.png">


This project on 3D morphologies builds on the 1D phase and introduces a new class called MAP(). MAP() generates a Pyrosim layout that is independent of Pyrosim, connecting multiple blocks while adhering to Pyrosim rules such as avoiding block intersections and ensuring that the first joint and link are absolute. The generation of every MAP class instance takes this rule into account.

The algorithm for generating a new link and block to be added to the layout works as follows:

1. Randomly select a link.
2. Randomly select a face to which a new block can be added.
3. Generate the new link and block with both relative and absolute coordinates to avoid collisions.

The complete output of this process is displayed above, and an instance of the MAP class is created each time the SOLUTION class is initialized, granting access to the body of this class.

The neural network for this project remains largely unchanged from previous assignments. A random number of blocks contain sensors and motors, and the network is generated with a set of connections and random weights. This can be observed by adding an "exit()" at the end of Create_Brain() in the SOLUTION class. These random movements can later be evolved in conjunction with the randomly generated bodies.

It is worth noting that for this project, 1x1x1 cubes were used, but the current framework can easily be adapted to include blocks of random sizes. While cubes may look visually cleaner, other block shapes can be used.

To see how the MAP() class works, download the repository and run the map.py file. The main class allows for the creation of a map of any size and output display. To run the simulation, execute the search.py file.

For a demonstration of the project, refer to the YouTube video below, which showcases three bots in action:
https://www.youtube.com/shorts/q5DsHOAAVd8
