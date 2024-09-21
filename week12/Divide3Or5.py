"""mod doc"""
def main():
    """doc"""
    number = int(input())
    total = 0
    for i in range(1, int(number) + 1):
        if not i%3 or not i%5:
            total += i
    print(total)
main()
