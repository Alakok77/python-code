"""mod doc"""
def main():
    """doc"""
    card = int(input())
    total = 0
    for _ in range(card):
        point = input()
        if point == "A":
            total += 11
        elif point in "JKQ":
            total += 10
        else:
            total += int(point)
        if total > 21 and total != 30:
            total -= 10
    print(total)
main()
