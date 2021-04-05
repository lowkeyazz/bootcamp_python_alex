import sys


def operations(a, b):
    if not (a.isdigit() and b.isdigit()):
        print("InputError: only numbers \n\nUsage: python operations.py <number1> <number2>\n","Example:\n    python operations.py 10 3")
        return
    elif (a.isdigit() and b.isdigit()):
        print("Sum:         ", (float(a) + float(b)))
        print("Difference:  ", (float(a) - float(b)))
        print("Product:     ", (float(a) * float(b)))
        if (float(b) == 0):
            print("Quotient:     ERROR (div by zero)")
            print("Remainder:    ERROR (modulo by zero)")
        else:
            print("Quotient:    ", (float(a) / float(b)))
            print("Remainder:   ", (float(a) % float(b)))


if len(sys.argv) == 3:
    operations(sys.argv[1], sys.argv[2])
else:
    print("InputError: only numbers \n\nUsage: python operations.py <number1> <number2>\n","Example:\n    python operations.py 10 3")
