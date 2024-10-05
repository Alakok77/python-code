"""mod doc"""
def main():
    """doc"""
    k_var = int(input())
    human = int(input())
    total = {k_var : 0}
    for _ in range(human):
        point = int(input())
        if point not in total:
            total[point] = 1
        else:
            total[point] += 1
    point = list(total.values())
    draw = point.count(max(point)) > 1 or max(point) < human/2
    win = max(total, key= total.get)
    if draw:
        print(f"0 {max(total.values())}")
    else:
        print(f"{win} {total[win]}")
main()
