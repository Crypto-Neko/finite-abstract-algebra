from bin_op import *
from group import *

####################################################################################################################
# Represents an element of a FinAbGroup object. The only additional function is to replace multiplication with     #
# additon, since the operation of an abelian group is usually represneted with a "+" sign.                         #
#                                                                                                                  #
# ElementOfFAG.value: The value associated with the element, a tuple.                                              #
# ElementOfFAG.structure: The FinAbGroup object of which the ElementOfFAG object is an element.                    #
####################################################################################################################
class ElementOfFAG(Element):
    def __init__(self, value, structure):
        super().__init__(value, structure)

    # Override the __mul__ method in Element so that it doesn't work anymore.
    def __mul__(self, other):
        raise ValueError("Multiplication not defined.")

    # Use addition as the operation instead of multiplication because it's a FAG.
    def __add__(self, other):
        if isinstance(other, ElementOfFAG):
            return self.structure.multiply(self, other)


####################################################################################################################
# Implements a finite abelian group with an arbitrary number of generators. Constructs the FinAbGroup object with  #
# inheritance from the Group class. Takes as input a list of the order of the generators for the group, e.g.       #
# Z2xZ3 = FinAbGroup([2, 3]).                                                                                      #
#                                                                                                                  #
# FinAbGroup.construct_elements(tup, i): Recursively construct the tuple elements of the group in order of gens.   #
# FinAbGroup.construct_table(): Construct the table from the list of elements.                                     #
#                                                                                                                  #
# FinAbgroup.generators: A list of the orders of the generators of the Group.                                      #
# FinAbGroup.elements: The elements of the Group, represented with tuples as values.                               #
# FinAbGroup.table: The multiplication table of the Group.                                                         #
####################################################################################################################
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
            self.elements.append(ElementOfFAG(tup, self))
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
                row.append(ElementOfFAG(tup, self))
            table.append(row)

        self.table = table


    # Print the identify of the group in terms of a product of integer groups.
    def __str__(self):
        rep = ""
        for i in range(len(self.generators)):
            rep += "Z" + str(self.generators[i])
            if i != len(self.generators) - 1:
                rep += " x "

        return rep


    __repr__ = __str__
