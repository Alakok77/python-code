"""mod doc"""
def main():
    """doc"""
    txt = f"{input()}0"
    lst_gram = []
    for i, j in enumerate(txt):
        if j == "0":
            break
        if f"{j}{txt[i+1]}" not in lst_gram:
            lst_gram.append(f"{j}{txt[i+1]}")
    cnt = []
    for i in lst_gram:
        cnt.append(txt.count(i))
    most = lst_gram[cnt.index(max(cnt))]
    print(most)
    print(max(cnt))
main()
