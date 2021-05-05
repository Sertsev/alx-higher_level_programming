#!/usr/bin/python3
import sys
if __name__ == "__main__":
    x = len(sys.argv) - 1
    if x == 0:
        print("{:d} arguments.".format(x))
    else:
        if x == 1:
            print("{:d} argument:".format(x))
            for y in range(x):
                print("{:d}: {:s}".format(y+1, sys.argv[y+1]))
        else:
            print("{:d} arguments:".format(x))
            for y in range(x):
                print("{:d}: {:s}".format(y+1, sys.argv[y+1]))
