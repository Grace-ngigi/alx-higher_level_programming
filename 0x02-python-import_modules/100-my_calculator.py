#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if (len(sys.argv) != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit (1)
    else:
        if sys.argv[1] != '+' or sys.argv[1] != '-' or sys.argv[1] != '*' or sys.argv[1] != '/':
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        a = int(sys.argv[0])
        b = int(sys.argv[2])
        if sys.argv[1] == '+':
            print("{} + {} = {}".format(a, b, a + b))
        elif sys.argv[1] == '-':
            print("{} - {} = {}".format(a, b, a - b))
        elif sys.argv[1] == '*':
            print("{} * {} = {}".format(a, b, a * b))
        elif sys.argv[1] == '/':
            print("{} / {} = {}".format(a, b, a / b))
