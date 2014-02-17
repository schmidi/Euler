#!/usr/bin/env python


list = list()

for i in range(1, 1000):

    if i % 3 == 0 or i % 5 == 0:
        list.append(i)
total = 0
for i in list:
    total = total + i


print total