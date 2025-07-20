#!/usr/bin/env python3

def collatz(number):
    even = number % 2 == 0
    if even:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result

while True:
    collatz(int(input()))


