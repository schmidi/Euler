#!/usr/bin/env python


for c in range(1000, 0, -1):
    for b in range(c, 0, -1):
        a = 1000 - c - b

        if 0 < a < b and a ** 2 + b ** 2 == c ** 2:
            print a*b*c

