import random


class Link():
    def __init__(self, rel_pos, abs_pos, num, prev) -> None:
        self.rel = rel_pos
        self.abs = abs_pos
        self.name = "Link" + str(num)
        self.prev = None
        self.num = num

        #set first block to size 1,1,1, randomize the rest
        if num != 1: self.dims = [random.uniform(1.5, 2), random.uniform(1.5, 2), random.uniform(1.5, 2)]
        else: self.dims = [1,1,1]



        

