import sys


def oddchecker(a):
    n = int(a)
    if n == 0:
        print("I'm zero.")
    elif n % 2 == 0:
        print("I'm even.")
    elif n % 2 != 0:
        print("I'm odd.")
    else:
        print("ERROR")


if len(sys.argv[1:]) == 1:
    if sys.argv[1].isdigit():
        oddchecker(sys.argv[1])
    else:
        print("ERROR")
else:
    print("ERROR")
