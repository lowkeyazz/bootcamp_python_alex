def operations(a, b):
    if (not (((type(a) == int) or (type(a) == float)) and ((type(b) == int) or (type(b) == float)))):
        print("InputError: only numbers \n\nUsage: python operations.py <number1> <number2>\n"
              "Example:\n    python operations.py 10 3")
        return
    elif (((type(a) == int) or (type(a) == float)) and ((type(a) == int) or (type(a) == float))):
        print("Sum:         ", (a + b))
        print("Difference:  ", (a - b))
        print("Product:     ", (a * b))
        if (b == 0):
            print("Quotient:     ERROR (div by zero)")
            print("Remainder:    ERROR (modulo by zero)")
        else:
            print("Quotient:    ", (a / b))
            print("Remainder:   ", (a % b))
