#!/usr/bin/env python3

def comma(lis):
    string = ""

    for index, item in enumerate(lis):
        string += item
        if index == len(lis) - 2:
            string += " and "
        elif index < len(lis) - 1:
            string += ", "
    print(string)
    return(string)

comma(["A", "B", "C"])
