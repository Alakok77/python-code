"""mod doc"""
def cal(number, cnt):
    """doc"""
    if number < 2:
        return cnt
    if not number%2:
        cnt += 1
        return cal(number/2, cnt)
    cnt += 1
    return cal((number * 3) + 1, cnt)
def main():
    """main function""" 
    while True:
        num = int(input())
        if not num:
            break
        print(cal(num, 1))

main()
