#!/usr/bin/env python

maxCount = 1000000


def next_number(n):

    assert n >= 0

    if n % 2 == 0:
        return n / 2
    else:
        return 3*n + 1

results = dict()

for i in range(1, maxCount):

    value = i
    chain = list()

    while value != 1:
        chain.append(value)
        value = next_number(value)

    results[i] = len(chain)

sorted_results = sorted(results.items(), key=lambda x:x[1])

print sorted_results[-1]


