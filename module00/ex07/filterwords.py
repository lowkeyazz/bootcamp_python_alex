import sys


def filter(txt, l):
    words = []
    wordi = ""
    for i in range(len(txt)):
        if txt[i].isalpha():
            wordi += txt[i]
            if i == len(txt)-1:
                words.append(wordi)
        else:
            words.append(wordi)
            wordi = ""
    tabwords = []
    for i in words:
        if len(i) > l:
            tabwords.append(i)
    return tabwords


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("ERROR")
    else:
        if sys.argv[1].isdigit():
            print("ERROR")
        else:
            if sys.argv[2].isdigit():
                print(filter(sys.argv[1], int(sys.argv[2])))
            else:
                print("ERROR")
