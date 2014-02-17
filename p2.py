#!/usr/bin/env python

list = [1]
i = 1

while i < 4000000:

    if i == 1:
        i = 2
    elif i == 2:
        i += list[0]
    else:
        i = list[len(list)-1] + list[len(list)-2]
    list.append(i)

total = 0
for i in list:
    if i % 2 == 0:
        total += i

print total

