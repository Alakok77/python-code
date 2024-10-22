"""mod doc"""
def main():
    """doc"""
    txt = input()
    inverse = txt[-1::-1]
    for i in inverse:
        if i in ("a", "e", "i", "o", "u"):
            if inverse.index(i) == len(txt) - 1:
                inverse = inverse[:inverse.index(i)] + i*4
            else:
                inverse = inverse[:inverse.index(i)] + i*4 + inverse[inverse.index(i) + 1:]
            break
    print(inverse[-1::-1])
main()
