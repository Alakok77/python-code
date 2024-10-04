"""mod doc"""
def main():
    """doc"""
    old = input()
    new = input()
    cnt = 0
    for i, j in enumerate(old):
        if j != new[i]:
            cnt += 1
    print(cnt)
main()
