"""mod doc"""
def main():
    """doc"""
    num = int(input())
    txt = ""
    for _ in range(num):
        txt = input()
        if txt.count("ka") + txt.count("ba") + txt.count("ta") + txt.count("bakka"):
            print("yes")
        else:
            print("no")
main()
