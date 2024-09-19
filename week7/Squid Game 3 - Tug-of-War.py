"""mod doc"""
def main():
    """doc"""
    a = 0
    b = 0
    for _ in range(10):
        a += int(input())
    for _ in range(10):
        b += int(input())
    if a > b:
        print("B")
    elif a < b:
        print("A")
    else:
        print("AB")
main()
