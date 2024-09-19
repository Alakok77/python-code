"""mod doc"""
def main():
    """doc"""
    text = input()
    check = f"{text}!"
    old = ""
    result = ""
    cnt = 0
    for i in check:
        if i == old:
            cnt += 1
        else:
            result += str(cnt)
            cnt = 1
            result += old
        old = i
    print(result[1:])
main()
