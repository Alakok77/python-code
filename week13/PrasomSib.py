"""mod doc"""
def main():
    """doc"""
    num = f"{input()}000"
    cnt = 0
    for i, j in enumerate(num):
        if j == "0":
            break
        if int(j) + int(num[i+1]) == 10:
            cnt += 1
        elif int(j) + int(num[i+1]) + int(num[i+2]) == 10:
            cnt += 1
        elif int(j) + int(num[i+1]) + int(num[i+2]) + int(num[i+3]) == 10:
            cnt += 1
    print(cnt)
main()
