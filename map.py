import numpy as np
from joint import Joint
from link import Link
import random


class MAP():
    def __init__(self, numlinks) -> None:
        self.list_links = set()
        self.list_joints = set()
        self.numlinks = numlinks
        self.create_first_link()
        self.generate()

    def create_first_link(self):
        link0 = Link(rel_pos = None, abs_pos=np.array([0,0,1]), num = 0, prev=None)
        self.list_links.add(link0)

    def generate(self):
        while len(self.list_links) < self.numlinks:
            self.find_new_joint_and_link()

    def find_new_joint_and_link(self):
        #pick a random link and face
        parent_link = random.choice(list(self.list_links))
        rand_face = random.randint(1,6)
        result = self.generate_new_link_and_joint(parent_link, rand_face)
        #invalid link generated
        if result == False: return
        #otherwise
        else:
            new_link = result[0]
            new_joint = result[1]
        #using generate_new_link_and_joint
            #calculate the new absolute position of this random block and face
        
            #if this absolute position is intersecting another block or ground, return and try again
        #add the joint and the new link to the map were done
        self.list_links.add(new_link)
        self.list_joints.add(new_joint)

    def generate_new_link_and_joint(self, parent_link, rand_face):
        axis_list = ["0 1 0", "0 1 0", "1 0 0", "1 0 0", "0 0 1", "0 0 1"]
        new_joint_axis = axis_list[rand_face - 1]
        #-----if it is the first link, use absolute positions to calculate absolute position of next block-------
        if parent_link.num == 0:
            if rand_face == 1:
                new_abs_joint = np.array([0.5,0,1])
                new_abs_block = parent_link.abs + np.array([1,0,0])
                new_rel_block = np.array([0,0,0.5])
            elif rand_face == 2:
                new_abs_joint = np.array([-0.5,0,1])
                new_abs_block = parent_link.abs + np.array([-1,0,0])
                new_rel_block = np.array([0,0,0.5])
            elif rand_face == 3:
                new_abs_joint = np.array([0,0.5,1])
                new_abs_block = parent_link.abs + np.array([0,1,0])
                new_rel_block = np.array([0,0.5,0])
            elif rand_face == 4:
                new_abs_joint = np.array([0,-0.5,1])
                new_abs_block = parent_link.abs + np.array([0,-1,0])
                new_rel_block = np.array([0,0.5,0])
            elif rand_face == 5:
                new_abs_joint = np.array([0,0,1.5])
                new_abs_block = parent_link.abs + np.array([0,1,0])
                new_rel_block = np.array([0,0.5,0])
            elif rand_face == 6:
                return False
            new_link = Link(rel_pos=new_rel_block, abs_pos=new_abs_block, num=len(self.list_links), prev=parent_link)
            new_joint = Joint(num = len(self.list_joints), rel_pos=None, abs_pos=new_abs_joint, parent = parent_link, child = new_link, face=rand_face, axis=new_joint_axis)
            return new_link, new_joint

        #------else calculate the new absolute position of this random block and face-----
        else:
            prev_face = self.get_prev_face(parent_link)
            #now generate new absolute positions and relative positions
            x1 = parent_link.abs[0]
            y1 = parent_link.abs[1]
            z1 = parent_link.abs[2]
            if prev_face == 1:
                if rand_face == 1:
                    new_abs_block = np.array([x1+1, y1, z1])
                    new_rel_block = np.array([0.5, 0, 0])
                    new_rel_joint = np.array([1, 0, 0])
                if rand_face == 2:
                    return False
                if rand_face == 3:
                    new_abs_block = np.array([x1, y1+1, z1])
                    new_rel_block = np.array([0, 0.5, 0])
                    new_rel_joint = np.array([0.5, 0.5, 0])
                if rand_face == 4:
                    new_abs_block = np.array([x1, y1-1, z1])
                    new_rel_block = np.array([0, -0.5, 0])
                    new_rel_joint = np.array([0.5, -0.5, 0])
                if rand_face == 5:
                    new_abs_block = np.array([x1, y1, z1 +1])
                    new_rel_block = np.array([0,0,0.5])
                    new_rel_joint = np.array([0.5, 0, 0.5])
                if rand_face == 6:
                    new_abs_block = np.array([x1, y1, z1 - 1])
                    new_rel_block = np.array([0,0,0.5])
                    new_rel_joint = np.array([0.5, 0, 0.5])


    def get_prev_face(self, parent_link):
        for joint in self.list_joints:
            if joint.child.num == parent_link.num:
                return joint.face
                


    


if __name__ == '__main__':
    map = MAP(numlinks = 2)
    for link in map.list_links:
        print("-------------------------links----------------------------")
        print(link.name + "   Abs pos:   " + str(link.abs) + "   Rel pos:   " + str(link.rel))
    for joint in map.list_joints:
        print("-------------------------joints----------------------------")
        print(joint.name + "   Abs pos:   " + str(joint.abs) + "   Rel pos:   " + str(joint.rel) + "       face:   " + str(joint.face))