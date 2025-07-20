#!/usr/bin/env python3

char = input("Enter the character to be repeated: ")
width = int(input("Enter the width of the stream: "))
tq = int(input("Enter number of half a turn: "))
#sbc = 0

t = []
for up in range(tq+1):
    t.append(up)
for down in range(tq-1,0,-1):
    t.append(down)

while True:
    for sbc in t:
        print(" " * 10 + "|" + " " * sbc + char * width)

