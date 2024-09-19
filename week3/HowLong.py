"""mod doc"""
def main():
    """doc"""
    num = abs(int(input()))
    nub = 1
    while num > 9:
        num /= 10
        nub += 1
    print(nub)
main()
