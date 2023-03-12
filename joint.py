import random
from link import Link

class Joint():
    def __init__(self, num, rel_pos, abs_pos, parent, child, axis, face):
        self.num = num
        self.rel = rel_pos
        self.abs = abs_pos
        self.parent = parent
        self.child = child
        self.axis = axis
        self.face = face
        self.name = self.parent.name + "_" + self.child.name

    def fix_name(self):
        self.name = self.parent.name + "_" + self.child.name