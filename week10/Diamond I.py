"""mod doc"""
def main():
    """doc"""
    floor = int(input())
    field = int(input())
    step = ""
    total = []
    for _ in range(field):
        total.append(0)
    for _ in range(floor):
        step = input().split()
        for _ ,j in enumerate(step):
            total.append(int(j) + int(total[0]))
            total.pop(0)
    print(max(total))
main()
