"""mod doc"""
def main():
    """doc"""
    people = int(input())
    lift_weight = float(input())
    total_weight = 0
    old = 0
    weight = 0
    safe = False
    for _ in range(people):
        old = int(input())
        weight = float(input())
        total_weight += weight
        if old >= 12:
            safe = True
    if total_weight <= lift_weight and safe:
        print("Safe")
    elif not people:
        print("Safe")
    else:
        print("Not Safe")
main()
