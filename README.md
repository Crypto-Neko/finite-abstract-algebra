# Finite Abstract Algebra

Here begins my personal project to implement all abstract algebra in Python! There are three main reasons I'm doing this, listed from least to most important:

1. It could perhaps be helpful with some of my homework for advanced algebra homework.
2. I want to write a finite fields implementation myself for cryptography with elliptic curves because when I implemented ECC on my own I realized after the fact that it obviously could not work for fields with prime power order (not prime order).
3. It will be fun!!

I've chosen to make everything associative because I'd probably need to use a stack or something to implement non-associative algebra and that would be way too much work when what I care about is everything from groups upward, so I'm going to start with associative binary operations and then work my way up to fields etc. I'm mostly going to work with finite groups, but when moving to modules, FDVS, fields, etc. I will find a way to work with infinite objects.

Here's a map of everything I've done so far:

* Algebraic Structures
  * bin_op.py -- Element, BinOp
  * group.py -- Group
* Geometry
  * Symmetry Groups
    * klein-4.py -- K: Klein-4 group
  * Elliptic Curves
* Number theory
  * Number Groups
    * Z2xZ2.py: Z2xZ2: The Cartesian product of Z2 with itself as a group
