"""mod doc"""
def main():
    """doc"""
    txt = ""
    lst = []
    friend = {}
    while True:
        txt = input()
        if "?" in txt:
            lst = txt.split(" ? ")
            break
        lst = txt.split(" <-> ")
        if lst[0] not in friend:
            friend[lst[0]] = lst[1]
        elif lst[0] in friend:
            friend[lst[0]] = f"{friend[lst[0]]}+{lst[1]}"
        if lst[1] not in friend:
            friend[lst[1]] = lst[0]
        elif lst[1] in friend:
            friend[lst[1]] = f"{friend[lst[1]]}+{lst[0]}"
    if lst[0] not in friend or lst[1] not in friend:
        z = []
    else:
        a = set(friend[lst[0]].split("+"))
        b = set(friend[lst[1]].split("+"))
        z = sorted(list(a&b), key= str, reverse=True)
    if len(z) > 0:
        for i in list(a&b):
            print(i)
    else:
        print("No mutual friend")
main()
