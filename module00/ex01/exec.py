import sys


def reverse(x):
    new = []
    for i in x[::-1]:
        if i.isupper():
            new.append(i.lower())
        elif i.islower():
            new.append(i.upper())
        else:
            new.append(i)
    return new


txt = ' '.join(sys.argv[1:])
l = len(txt)
if l > 1:
    mytxt = reverse(txt)
    print(''.join(mytxt))
