"""mod doc"""
def main():
    """doc"""
    text = input()
    alpha = ""
    remain = ""
    for i in text:
        if i not in alpha:
            alpha += i
    for i in alpha:
        if text.count(i) % 2:
            remain += i
    if len(remain) > 0:
        for i in remain:
            print(i, end = "")
    else:
        print("fully paired")
main()
