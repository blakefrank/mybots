![Page1](https://user-images.githubusercontent.com/86979153/220497788-6b1c6484-cf55-4c19-acce-27e7383ae580.jpg)
![Page2](https://user-images.githubusercontent.com/86979153/220497814-dca0bab5-d950-4bff-9581-ddae9109d0d5.jpg)
<img width="842" alt="Screen Shot 2023-02-21 at 7 34 11 PM" src="https://user-images.githubusercontent.com/86979153/220498078-baafafa7-b00a-4806-9945-9c3ac0f29256.png">


This 3d-morphologies project is an extension of the 1-d phase. I implemented an entire new class called MAP(), which essentially generates a pyrosim layout completely independent of pyrosim, connecting a bunch of blocks such that none intersect and all other rules of pyrosim are followed. Other rules include that the first joint and link must be absolute, which is taken into account in the generation of every instance of the MAP class. 

The algorithm works as follows:

1. Pick a random link
2. pick a random face to add a new block
3. (and now the hard part) Generate the new link and block with relative AND absolute coordinate to avoid collisions.

The complete output of this is shown above. An instance of the MAP class is created every time the SOLUTION class is initialized, allowing us access to the boy of this class. 

The neural network was not changed much from previous assignments. A random number of blocks contain sensor and motors, and the network is generated with a series of connections and random weights. This can be seen by adding an "exit()" at the end of Create_Brain() in the SOLUTION class. These random movement can later be evolved along with the randomly generated bodies.

Note: for this project I used 1x1x1 cubes, but this can easily be adapted with the current framework to random size blocks. Cubes will probably look the cleanest, visually.
