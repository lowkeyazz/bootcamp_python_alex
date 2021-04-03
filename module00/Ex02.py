def oddchecker(n):
    if type(n)!=float:
        print("ERROR")
    elif n%2==0:
        print("I'm even.")
    elif n%2!=0:
        print("I'm odd.")
    elif n==0:
        print("I'm zero.")
