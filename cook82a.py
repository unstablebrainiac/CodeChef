#!/usr/bin/python3

t = int(input())
for i in range(t):
    for j in range(4):
        team,score = input().split()
        if team == "Barcelona":
            bar = score
        elif team == "Malaga":
            mal = score
        elif team == "RealMadrid":
            rea = score
        elif team == "Eibar":
            eib = score
    if rea < mal and bar > eib:
        print("Barcelona")
    else:
        print("RealMadrid")
