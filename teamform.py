#!/usr/bin/python3

num = int(input())
for i in range(num):
    n,m = input().split()
    n = int(n)
    m = int(m)
    for i in range(m):
        input()
    if n % 2 == 0:
        print("yes")
    else:
        print("no")
