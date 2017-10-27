#!/usr/bin/python3

t = int(input())
for i in range(t):
    u,v = input().split()
    u = int(u)
    v = int(v)
    print(int((u+v)*(u+v+1)/2 + 1 + u))
