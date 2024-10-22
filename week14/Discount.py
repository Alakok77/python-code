"""mod doc"""
def main():
    """doc"""
    price = 0
    lst = []
    while True:
        price = input()
        if price == "ENTER":
            break
        lst.append(int(price))
    cnt = len(lst)
    lst.sort()
    if cnt <= 20:
        if cnt < 6:
            cnt = 0
        elif 5 < cnt < 11:
            cnt = 1
        elif 12 <= cnt < 20:
            cnt = 2
        else:
            cnt = 4
        total = sum(lst[cnt:])
    else:
        total = sum(lst[cnt//5:])
    print(total)
main()
