def text_analyzer(a):
    up = 0
    low = 0
    spc = 0
    pnc = 0
    num = 0
    for i in a:
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
        elif i.isspace():
            spc += 1
        elif i.isdigit():
            num += 1
        else:
            pnc += 1
    allch = up+low+pnc+num+spc
    print("The text contains ", allch, " characters:", sep="")
    print("-", up, " upper letters", sep="")
    print("-", low, " lower letters", sep="")
    print("-", pnc, " punctuation marks", sep="")
    print("-", spc, " spaces", sep="")
