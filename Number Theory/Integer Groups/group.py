from bin_op import *

# The error that will be used for when the definition of a structure is not met by its construction.
class DefinitionError(Exception):
    pass


####################################################################################################################
# Implements a Group object
#
#
#
####################################################################################################################
class Group(BinOp):
    def __init__(self, elements, table):
        # Initialize the Group as a BinOp.
        super().__init__(elements, table)

        # Check if the identity element exists and is in the right place.
        i = 0
        while i < len(table):
            if not table[0][i] == elements[i] or not table[i][0] == elements[i]:
                raise DefinitionError("The first element must be identity and the group must have an identity!")
            i+=1

        # Check that identity is unique.
        row1 = table[0]
        count = 0
        for row in table:
            if row == row1:
                count +=1
        if count != 1:
            raise DefinitionError("Identity must be unique!")

        # Check that every row contains identity exactly once, i.e. there is an inverse for each element and it is unique.
        for row in table:
            identityExists = 0
            for element in row:
                if element == elements[0]:
                    identityExists = 1
            if identityExists != 1:
                raise DefinitionError("Every element must have a unique inverse!")

    # Checks if the group is commutative, returning True when it is and False otherwise.
    def is_commutative(self):
        bad = 0
        i = 0
        while i < len(self.table):
            j = 0
            while j < len(self.table):
                if self.table[i][j] != self.table[j][i]:
                    bad+=1
                j+=1
            i+=1

        if bad > 0:
            return False
        return True

    # Checks if two curves are isomorphic to one another, returning True if so and False otherwise.
    def is_isomorphic(self, other):
        # Check that other is a group and that the cardinality is the same.
        if not isinstance(other, Group):
            return "Error: isomorphisms must be between groups!"
        if not len(self.elements) == len(other.elements):
            return 0

        # Index the elements of each group so that comparing multiplication tables is possible.
        self_indices = {}
        for element in self.elements:
            if not element in self_indices:
                self_indices[element] = len(self_indices)
        other_indices = {}
        for element in other.elements:
            if not element in other_indices:
                other_indices[element] = len(other_indices)

        # Replace the elements in each multiplication table with the index of each element.
        self_table = []
        for row in self.table:
            rowToAdd = []
            for element in row:
                rowToAdd.append(self_indices[element])
            self_table.append(rowToAdd)
        other_table = []
        for row in other.table:
            rowToAdd = []
            for element in row:
                rowToAdd.append(other_indices[element])
            other_table.append(rowToAdd)

        # Compare the two matrices, making sure they are the same up to a permutation of rows.
        rowsAccountedFor = 0
        for row1 in self_table:
            for row2 in other_table:
                if row1 == row2:
                    rowsAccountedFor+=1

        if rowsAccountedFor == len(self.table):
            return True
        return False
        

    def __eq__(self, other):
        return (self.elements == other.elements and self.table == other.table)
