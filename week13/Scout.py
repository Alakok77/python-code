"""mod doc"""
def main():
    """doc"""
    test = int(input())
    info, weight = [], []
    cnt, check = 0, 0
    for _ in range(test):
        info = list(map(int, input().split()))
        weight = sorted(list(map(int, input().split())))
        for i, j in enumerate(weight):
            check += int(j)
            if i + 1 > int(info[1]) or check > int(info[2]):
                break
            cnt += 1
        print(cnt)
        cnt, check = 0, 0
main()
