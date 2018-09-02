#!/usr/bin/env python3

# Prints a list of numbers between [77, 777] which are divisible by 7 but not 5
result = []
for n in range(77, 778):
    if n % 5 == 0:
        continue
    elif n % 7 == 0:
        result.append(n)
print(result)
