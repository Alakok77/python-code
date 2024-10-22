"""mod doc"""
def main():
    """doc"""
    dump = input()
    check = {}
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in alpha:
        if i in dump:
            check[i] = dump.count(i)
    for key, value in check.items():
        if value % 2:
            check[key] = value - 1
    result = ""
    for key, value in check.items():
        result += key * value
    cnt = ""
    none = True
    for i in check.values():
        if not i % 2 and i:
            none = False
    if none:
        print("None")
        print(0)
    else:
        for i in result:
            if len(cnt) == 2:
                print(f" {i}", end = "")
                cnt = ""
                cnt += i
            else:
                print(i, end = "")
                cnt += i
        print("")
        print(int(sum(check.values())/2))
main()
