"""mod doc"""
def main():
    """doc"""
    hour = int(input())
    minute = int(input())
    gap = ((hour * 30) + (minute * 0.5)) - (minute * 6)
    if 0 <= gap < 6:
        print("True")
        return
    print("False")
main()
