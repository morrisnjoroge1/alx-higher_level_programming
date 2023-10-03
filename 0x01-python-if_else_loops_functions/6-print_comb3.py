#!/usr/bin/python3
for b in range(0, 10):
    for c in range((b+1), 10):
        if (b != 8) or (c != 9):
            print("{}{}, ".format(b, c), end="")
        else:
            print("{}{}".format(b, c))
