#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_arg = len(argv)
    if num_arg == 1:
        print("{} arguments.".format(num_arg - 1))
    else:
        print("{} arguments:".format(num_arg - 1))
        for i, arg in enumerate(argv):
            if i == 0:
                continue
            else:
                print("{}: {}".format(i, argv[i]))
