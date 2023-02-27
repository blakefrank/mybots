import numpy as np
from joint import Joint
from link import Link
import random
import copy


class MAP():
    def __init__(self, numlinks) -> None:
        self.list_links = list()
        self.list_joints = list()
        self.numlinks = numlinks
        self.create_first_link()
        self.generate()

    def create_first_link(self):
        link0 = Link(rel_pos = None, abs_pos=np.array([0,0,1]), num = 0, prev=None)
        self.list_links.append(link0)

    def generate(self):
        while len(self.list_links) < self.numlinks:
            self.find_new_joint_and_link()

    def find_new_joint_and_link(self):
        #pick a random link and face
        parent_link = random.choice(self.list_links)
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
        self.list_links.append(new_link)
        self.list_joints.append(new_joint)

    def generate_new_link_and_joint(self, parent_link, rand_face):
        axis_list = ["0 1 0", "0 1 0", "1 0 0", "1 0 0", "0 0 1", "0 0 1"]
        new_joint_axis = axis_list[rand_face - 1]
        #New Link (block) position
        x1 = parent_link.abs[0]
        y1 = parent_link.abs[1]
        z1 = parent_link.abs[2]
        if rand_face == 1:
            new_abs_block = np.array([x1 + 1, y1, z1])
            new_rel_block = np.array([0.5, 0,   0])
            
        if rand_face == 2:
            new_abs_block = np.array([x1-1, y1, z1])
            new_rel_block = np.array([-0.5, 0, 0])
            
        if rand_face == 3:
            new_abs_block = np.array([x1, y1+1, z1])
            new_rel_block = np.array([0, 0.5, 0])
            
        if rand_face == 4:
            new_abs_block = np.array([x1, y1-1, z1])
            new_rel_block = np.array([0, -0.5, 0])
            
        if rand_face == 5:
            new_abs_block = np.array([x1, y1, z1+1])
            new_rel_block = np.array([0,  0,   0.5])
        
        if rand_face == 6:
            new_abs_block = np.array([x1, y1, z1-1])
            new_rel_block = np.array([0, 0, -0.5])
        #-----if it is the first link, use absolute positions to calculate absolute position of next block-------
        if parent_link.num == 0:
            if rand_face == 1:
                new_abs_joint = np.array([0.5,0,1])
            elif rand_face == 2:
                new_abs_joint = np.array([-0.5,0,1])
            elif rand_face == 3:
                new_abs_joint = np.array([0,0.5,1])
            elif rand_face == 4:
                new_abs_joint = np.array([0,-0.5,1])
            elif rand_face == 5:
                new_abs_joint = np.array([0,0,1.5])
            elif rand_face == 6:
                return False
            if not self.is_valid_position(new_abs_block):
                return False
            new_link = Link(rel_pos=new_rel_block, abs_pos=new_abs_block, num=len(self.list_links), prev=parent_link)
            new_joint = Joint(num = len(self.list_joints), rel_pos=None, abs_pos=new_abs_joint, parent = parent_link, child = new_link, face=rand_face, axis=new_joint_axis)
            return new_link, new_joint

        #------else calculate the new absolute position of this random block and face-----
        else:
            prev_face = self.get_prev_face(parent_link)
            #now generate new absolute positions and relative positions
            
            #calc joint positions
            if prev_face == 1:
                if rand_face == 1:
                    new_rel_joint = np.array([1, 0, 0])
                if rand_face == 2:
                    return False
                if rand_face == 3:
                    new_rel_joint = np.array([0.5, 0.5, 0])
                if rand_face == 4:
                    new_rel_joint = np.array([0.5, -0.5, 0])
                if rand_face == 5:
                    new_rel_joint = np.array([0.5, 0, 0.5])
                if rand_face == 6:
                    new_rel_joint = np.array([0.5, 0, -0.5])

            if prev_face == 2:
                if rand_face == 1:
                    return False
                if rand_face == 2:
                    new_rel_joint = np.array([-1,   0, 0])
                if rand_face == 3:
                    new_rel_joint = np.array([-0.5, 0.5, 0])
                if rand_face == 4:
                    new_rel_joint = np.array([-0.5, -0.5, 0])
                if rand_face == 5:
                    new_rel_joint = np.array([-0.5, 0, 0.5])
                if rand_face == 6:
                    new_rel_joint = np.array([-0.5, 0, -0.5])

            if prev_face == 3:
                if rand_face == 1:
                    new_rel_joint = np.array([0.5, 0.5, 0])
                if rand_face == 2:
                    new_rel_joint = np.array([-0.5, 0.5, 0])
                if rand_face == 3:
                    new_rel_joint = np.array([0, 1,   0])
                if rand_face == 4:
                    return False
                if rand_face == 5:
                    new_rel_joint = np.array([0,  0.5, 0.5])
                if rand_face == 6:
                    new_rel_joint = np.array([0,  0.5, -0.5])

            if prev_face == 4:
                if rand_face == 1:
                    new_rel_joint = np.array([0.5, -0.5, 0])
                if rand_face == 2:
                    new_rel_joint = np.array([-0.5, -0.5, 0])
                if rand_face == 3:
                    return False
                if rand_face == 4:
                    new_rel_joint = np.array([0,   -1,   0])
                if rand_face == 5:
                    new_rel_joint = np.array([0, -0.5, 0.5])
                if rand_face == 6:
                    new_rel_joint = np.array([0, -0.5, -0.5])

            if prev_face == 5:
                if rand_face == 1:
                    new_rel_joint = np.array([0.5, 0, 0.5])
                if rand_face == 2:
                    new_rel_joint = np.array([-0.5, 0, 0.5])
                if rand_face == 3:
                    new_rel_joint = np.array([0,  0.5,  0.5])
                if rand_face == 4:
                    new_rel_joint = np.array([0, -0.5, 0.5])
                if rand_face == 5:
                    new_rel_joint = np.array([0,  0,    1])
                if rand_face == 6:
                    return False
            
            if prev_face == 6:
                if rand_face == 1:
                    new_rel_joint = np.array([0.5, 0, -0.5])
                if rand_face == 2:
                    new_rel_joint = np.array([-0.5, 0, -0.5])
                if rand_face == 3:
                    new_rel_joint = np.array([0, 0.5, -0.5])
                if rand_face == 4:
                    new_rel_joint = np.array([0, -0.5, -0.5])
                if rand_face == 5:
                    return False
                if rand_face == 6:
                    new_rel_joint = np.array([0, 0, -1])
            
            
            #finally, need to check_pos(new_absolute_block position)
            if not self.is_valid_position(new_abs_block):
                return False
            new_link = Link(rel_pos=new_rel_block, abs_pos=new_abs_block, num=len(self.list_links), prev=parent_link)
            new_joint = Joint(num=len(self.list_joints), rel_pos=new_rel_joint, abs_pos=None, parent = parent_link, child= new_link, axis = new_joint_axis, face= rand_face)
            return new_link, new_joint

    def is_valid_position(self, new_pos):
        for link in self.list_links:
            abs_pos = link.abs
            if self.dist(new_pos, abs_pos) < 1:
                return False
            elif new_pos[2] < 0.4:
                return False
        return True

    def dist(self, point1, point2):
        return np.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 + (point1[2]-point2[2])**2)

    def get_prev_face(self, parent_link):
        for joint in self.list_joints:
            if joint.child.num == parent_link.num:
                return joint.face

    def remove_edge_block(self):
        edge_links = copy.deepcopy(self.list_links)
        for joint in self.list_joints:
            joint_name = joint.parent.name
            for link in edge_links:
                if link.name == joint_name:
                    edge_links.remove(link)
        link_to_remove = random.choice(edge_links)
        for joint in self.list_joints:
            if joint.child.name == link_to_remove.name:
                joint_to_remove = joint
        for link in self.list_links:
            if link.name == link_to_remove.name:
                self.list_links.remove(link)
        
        for joint in self.list_joints:
            if joint_to_remove.name == joint.name:
                self.list_joints.remove(joint)
            



            



                


    


if __name__ == '__main__':
    map = MAP(numlinks=5)
    print("-------------------------links----------------------------")
    for link in map.list_links:
        print("{:<15}Abs pos: {:<25}Rel pos: {}".format(link.name, str(link.abs), str(link.rel)))
    print("-------------------------joints----------------------------")
    for joint in map.list_joints:
        print("{:<15}Abs pos: {:<25}Rel pos: {:<25}face: {}".format(joint.name, str(joint.abs), str(joint.rel), str(joint.face)))
    map.remove_edge_block()
    print("-------------------------links----------------------------")
    for link in map.list_links:
        print("{:<15}Abs pos: {:<25}Rel pos: {}".format(link.name, str(link.abs), str(link.rel)))
    print("-------------------------joints----------------------------")
    for joint in map.list_joints:
        print("{:<15}Abs pos: {:<25}Rel pos: {:<25}face: {}".format(joint.name, str(joint.abs), str(joint.rel), str(joint.face)))
