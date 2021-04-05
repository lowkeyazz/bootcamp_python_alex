def reverse(x):
    new=[]
    for i in x [::-1]:
        if i.isupper():
            new.append(i.lower())
        elif i.islower():
            new.append(i.upper())
        else:
            new.append(i)
    return new
text=input()
mytxt = reverse(text)
print (''.join(mytxt))
