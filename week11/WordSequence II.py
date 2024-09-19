"""mod doc"""
def main():
    """doc"""
    primary = input()
    target = input()
    if len(primary) >= len(target):
        for i in range(len(primary)+1):
            print(f"{target[0:i]}{primary[i:]}")
    else:
        for i in range(len(target)+1):
            print(f"{target[0:i]}{primary[i:]}")
main()
