"""mod doc"""
def main():
    """doc"""
    txt = input().split()
    pair = False
    for i in txt[-1::-1]:
        if not int(i)%3 or not int(i)%5:
            print(i)
            pair = True
    if not pair:
        print("Nope")
main()
