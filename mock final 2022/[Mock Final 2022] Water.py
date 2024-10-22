"""mod doc"""
def main():
    """doc"""
    month = int(input())
    price_per_unit = float(input())
    lower_unit = float(input())
    more_unit = float(input())
    free = float(input())
    usage = 0
    total = 0
    check = 0
    for _ in range(month):
        usage = float(input())
        if usage > lower_unit:
            check += price_per_unit*lower_unit + (usage - lower_unit) * more_unit
        else:
            check += usage * price_per_unit
        if check <= free:
            check = 0
        total += check
        check = 0
    print(f"{total:.2f}")
main()
