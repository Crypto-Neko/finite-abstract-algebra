import sys; sys.path.append(r"../../Algebraic Structures")
from bin_op import *
from group import *

e = Element('e')
a = Element('a')
b = Element('b')
ab = Element('ab')
elements = [e, a, b, ab]
table = [[e, a, b, ab], [a, e, ab, b], [b, ab, e, a], [ab, b, a, e]]
K = Group(elements, table)
