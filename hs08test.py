#!/usr/bin/python3

withdraw, amount = input().split()
withdraw = float(withdraw)
amount = float(amount)

if withdraw % 5 == 0:
    withdraw += 0.5
    if withdraw <= amount:
        amount -= withdraw
print(amount)
