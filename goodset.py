#!/usr/bin/python3

def isGood(set):
    last = set[-1]
    for i in range(len(set) - 1):
        diff = last - set[i]
        if diff in set and i != set.index(diff):
            return False
    return True

# @return The next number in the set of n elements
def next(set):
    if len(set) == 1:
        return 2
    last = set[-1]
    temp = last + 1
    while not isGood(set + [temp]):
        temp += 1
    return temp

def generateSet(n):
    if n == 1:
        return [1]
    set = generateSet(n-1)
    return set + [next(set)]

t = int(input())
for j in range(t):
    n = int(input())
    set = generateSet(n)
    for i in set:
        print(str(i), end = " ")
    print()
