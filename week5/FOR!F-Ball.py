"""mod doc"""
def main():
    """doc"""
    text = input()
    one = True
    two = False
    three = False
    for i in text:
        if i == "A":
            if one or two:
                two = not two
                one = not one
        elif i == "B":
            if two or three:
                three = not three
                two = not two
        elif i == "C":
            if one or three:
                one = not one
                three = not three
    if one:
        print(1)
    elif two:
        print(2)
    elif three:
        print(3)
main()
