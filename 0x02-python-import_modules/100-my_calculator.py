#!/usr/bin/python3

if __name__ == "__main__":
    """Imports all functions in calculator.py and handles basic operations"""
    import sys
    import calculator_1 as calc

    argv = sys.argv
    argc = len(argv)
    if argc != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        sys.exit(1)

    operators = "+-*/"
    for c in operators:
        if c == argv[2]:
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == "+":
        operation = calc.add
    elif argv[2] == "-":
        operation = calc.sub
    elif argv[2] == "*":
        operation = calc.mul
    elif argv[2] == "/":
        operation = calc.div

    print("{} {} {} = {}".format(a, argv[2], b, operation(a, b)))
