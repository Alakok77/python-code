"""mod doc"""
def main():
    """doc"""
    num = int(input())
    while num > 0:
        for j in range(7):
            j += 1
            if num > 0:
                print(num, end = " ")
                num -= 1
            else:
                break
        print("")
main()
