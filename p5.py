#!/usr/bin/env python

value = 20
oldValue = 0
run = True

while run:

    for i in range(1, 21):
        if not value % i == 0:
            value += 2
            break
        if i == 20 and value % i == 0:
            print value
            run = False

