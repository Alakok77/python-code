"""mod doc"""
def main():
    """doc"""
    num = int(input())
    txt = ""
    kabata = ("ka", "ba", "ta", "bakka")
    error = False
    for _ in range(num):
        txt = input()
        error = False
        while len(txt) and not error:
            if txt[0:5] in kabata:
                txt = txt[5:]
            elif txt[0:2] in kabata:
                if txt[0:4] == "baka":
                    error = True
                else:
                    txt = txt[2:]
            else:
                error = True
        if error:
            print("no")
        else:
            print("yes")
main()
