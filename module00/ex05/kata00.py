def aff(t):
    n=len(t)
    print("the",n," numbers are: ",end='')
    print(', '.join(str(i) for i in t))
t=(19,42,21)
aff(t)
