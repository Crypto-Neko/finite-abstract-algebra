from bin_op import *
from group import *

x0 = Element('(0, 0)')
x1 = Element('(1, 0)')
x2 = Element('(0, 1)')
x3 = Element('(1, 1)')
elements = [x0, x1, x2, x3]
table = [[x0, x1, x2, x3], [x1, x0, x3, x2], [x2, x3, x0, x1], [x3, x2, x1, x0]]
Z2xZ2 = Group(elements, table)
