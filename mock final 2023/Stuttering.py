"""mod doc"""
def main():
    """doc"""
    check = ""
    txt = input().split()
    result = ""
    for i in txt:
        if i != check:
            result += f"{i} "
        check = i
    print(result)
main()
