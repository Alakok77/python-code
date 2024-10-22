"""mod doc"""
def main():
    """doc"""
    lst = sorted([int(input()) for _ in range(3)])
    gap1 = lst[2] - lst[1]
    gap2 = lst[1] - lst[0]
    most = max(gap1, gap2)
    print(most-1)
main()
