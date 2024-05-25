from bin_op import *
from group import *

#######
#
#
#
#######
class FinAbGroup(Group):
    # Takes the list generators, containing the order of each generator.
    # Example: Z2 x Z6 = fag([2, 6])
    def __init__(self, generators):
        self.generators = generators
        self.elements = []
        self.table = []

        self.construct_elements((0,), 0)

    def construct_elements(self, element, gen):
        if gen == len(self.generators) - 1:
            i = 0
            while i < self.generators[gen]:
                self.elements.append(element + (self.generators[len(self.generators) -1],)
                i+=1

