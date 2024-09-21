"""mod doc"""
def main():
    """doc"""
    number = int(input())
    cnt = number
    for i in range(1, number + 1):
        for j in range(2, int(number**0.5) + 1):
            if not i % (j**2):
                cnt -= 1
                break
    print(cnt)
main()
