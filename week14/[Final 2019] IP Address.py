"""mod doc"""
def main():
    """doc"""
    ipv4 = f"{input()}&"
    pull = ""
    lst = []
    cond1 = False
    for i in ipv4:
        if i.isnumeric():
            pull += i
        elif i in (".", "&") and pull.isnumeric():
            pull = str(int(pull))
            lst.append(pull)
            pull = ""
        else:
            cond1 = True
    ipv4 = ".".join(lst)
    cond2 = len(lst) != 4
    cond3 = False
    for i in lst:
        if int(i) < 0 or int(i) > 255:
            cond3 = True
    if cond1 or cond2 or cond3:
        print("Invalid IPv4 address")
    else:
        print(ipv4)
main()
