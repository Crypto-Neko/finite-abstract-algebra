from bin_op import *
from group import *

#######
#
#
#
#######
class FinAbGroup(Group):
    # Takes the list generators, containing the order of each generator.
    # Example: Z2 x Z6 = FinAbGroup([2, 6])
    def __init__(self, generators):
        self.generators = generators
        self.elements = []
        self.table = []
        
        for i in range(self.generators[0]):
            self.construct_elements((i,), 0)
        
        self.construct_table()

        super().__init__(self.elements, self.table)


    # Construct the elements of the finite abelian group recursively.
    def construct_elements(self, tup, i):
        if i == len(self.generators) - 1:
            self.elements.append(Element(tup, self))
        else:
            for val in range(self.generators[i+1]):
                self.construct_elements(tup + (val,), i + 1)


    # Construct the table for the operation, standard addition.
    def construct_table(self):
        table = []
        for i in range(len(self.elements)):
            row = []
            for j in range(len(self.elements)):
                tup = tuple()
                for k in range(len(self.generators)):
                    tup += ((self.elements[i].value[k] + self.elements[j].value[k]) % self.generators[k]),
                row.append(Element(tup, self))
            table.append(row)

        self.table = table


    # Print the elements of the group.
    def __str__(self):
        return(str(self.elements))

    __repr__ = __str__
