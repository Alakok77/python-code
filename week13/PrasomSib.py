"""mod doc"""
def main():
    """doc"""
    num = f"{input()}000"
    cnt = 0
    for i, j in enumerate(num):
        if j == "0":
            break
        cond1 = int(j) + int(num[i + 1])
        cond2 = cond1 + int(num[i + 2])
        cond3 = cond2 + int(num[i + 3])
        if 10 in (cond1, cond2, cond3):
            cnt += 1
    print(cnt)
main()
