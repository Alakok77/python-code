"""mod doc"""
def main():
    """doc"""
    most = int(input())
    floor = int(input())
    total = most
    count = 0
    can_not = 0
    for i in range(floor):
        step = int(input())
        if step <= total:
            total -= step
            if not total:
                count += 1
                total += most
            if i == floor - 1:
                count += 1
        else:
            can_not += 1
    if count > 0:
        print(count)
    elif can_not > 0:
        print("No")
main()
