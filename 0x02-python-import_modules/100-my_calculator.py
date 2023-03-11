#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    if len(argv) != 4:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            exit(1)
    operator = argv[2]
    av_ops = {"+": add, "-": sub, "*": mul, "/": div}
    if operator not in av_ops:
        print("Unknown operator. Available operators: +, -, * and / f")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {} = {}".format(a, operator, b, av_ops[operator](a, b)))
