####################################################################################################################
# The Element class is extremely simple, necessary so that multiplication within an algebraic structure works.     #
# It simply holds an element of an algebraic structure.                                                            #
#                                                                                                                  #
# self.value: The value represented by the element, usually a char or string.                                      #
# self.structure: The structure to which the element belongs, a BinOp object.                                      #
####################################################################################################################
class Element():
    def __init__(self, value, structure=None):
        self.value = value
        self.structure = structure

    def __mul__(self, other):
        if isinstance(other, Element):
            return self.structure.multiply(self, other)

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, Element):
            return self.value == other.value

    __repr__ = __str__


####################################################################################################################
# Represents an associative binary operation, supporting multiplication with other elements of the set implemented #
# through a list of elements and a multiplication table.                                                           #
#                                                                                                                  #
# BinOp.multiply(other): Multiply two elements of the sructure.                                                    #
#                                                                                                                  #
# BinOp.elements: A list containing the elements of the structure.                                                 #
# BinOp.table: A table representing all possible pairs to multiply with the operation.                             #
####################################################################################################################
class BinOp():
    # Initialize operation with list of elements and multiplication table.
    def __init__(self, elements=[], table=[[]]):
        
        # Make sure elements is a list and table is a matrix. Ensure that table has the right dimensions.
        if not isinstance(elements, list) or not isinstance(table, list) or not isinstance(table[0], list):
            return "Make sure elements is the list of elements and table the multiplication table for the group."
        if not len(table[0]) == len(elements):
            return "Multiplication must be defined for every element!"
        
        for element in elements:
            element.structure = self
        self.elements = elements
        self.table = table  

    # Multiply two elements with the binary operation and return this element.
    def multiply(self, a, b):
            if a in self.elements and b in self.elements:
                apos = 0
                bpos = 0
                current = 0
                while current < len(self.elements):
                    if self.elements[current] == a:
                        apos = current
                    if self.elements[current] == b:
                        bpos = current
                    current+=1

                return self.table[apos][bpos]
            elif a not in self.elements or b not in self.elements:
                raise ValueError("BinOp not defined for one or more Elements.")
    
    def __str__(self):
        return str(self.elements)

    __repr__ = __str__
        
        
