"""mod doc"""
def main():
    """doc"""
    x = int(input())
    y =  0
    total = 0
    while y != -1:
        y = int(input())
        if y == -1:
            break
        total += y
        if total == x :
            break
    print(total)
main()
