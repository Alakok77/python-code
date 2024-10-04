"""mod doc"""
def main():
    """doc"""
    txt = f"{input()}0"
    gram = {}
    for i in range(len(txt) - 1):
        if i == "0":
            break
        check = f"{txt[i]}{txt[i+1]}"
        if check not in gram:
            gram[check] = 1
        else:
            gram[check] += 1
    most = max(gram, key= gram.get)
    print(most)
    print(gram[most])
main()
