"""mod doc"""
def condition(over1, x, y, cal):
    """doc"""
    if over1 == (x**2 + y**2)**0.5 or abs(over1 - cal) <= 0.01:
        print("Yes")
    else:
        print("No")
def main():
    """doc"""
    a = float(input())
    b = float(input())
    c = float(input())
    over = 0
    if a >= b:
        if a >= c:
            over = a
            cal = (b**2 + c**2)**0.5
            condition(over, b, c, cal)
        else:
            over = c
            cal = (a**2 + b**2)**0.5
            condition(over, a, b, cal)
    else:
        if b >= c:
            over = b
            cal = (a**2 + c**2)**0.5
            condition(over, a, c, cal)
        else:
            over = c
            cal = (a**2 + b**2)**0.5
            condition(over, a, b, cal)
main()
