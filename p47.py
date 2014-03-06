#/usr/bin/env python

from mathlib import MathLib

mathLib = MathLib()

for i in range(1000, 10000):

    list = list()
    mathLib.factorize(i, list)

    if len(list) > 4:
        # convert to set
        print "bla"
