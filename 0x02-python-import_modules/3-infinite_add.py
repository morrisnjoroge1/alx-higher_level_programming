#!/usr/bin/python3
 #Author morris njoroge

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = 0
    for z in range(len(sys.argv) - 1):
        total += int(sys.argv[z + 1])
    print("{}".format(total))
