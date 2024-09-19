"""mod doc"""
def main():
    """doc"""
    cat_lst = []
    check = []
    cat = ""
    while True:
        cat = input()
        if cat == "END":
            break
        if cat == "IT'S A DOG":
            cat_lst.pop()
            continue
        if "," in cat:
            cat_lst.extend(cat.split(", "))
        else:
            cat_lst.append(cat)
    sort_cat = sorted(cat_lst, key=str.lower)
    for i in sort_cat:
        if not i in check:
            print(f"{i} {cat_lst.index(i) + 1} {sort_cat.count(i)}")
        else:
            continue
        check.append(i)
main()
