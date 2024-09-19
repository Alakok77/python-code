"""mod doc"""
def main():
    """doc"""
    text = input().split()
    finder = input()
    for _ in range(text.count(finder)):
        for _ in range(text.count(finder)):
            print(text.index(finder), end=" ")
        print()
main()
