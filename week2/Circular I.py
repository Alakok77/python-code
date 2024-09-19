"""mod doc"""
import math
def main():
    """doc"""
    xm = float(input())
    ym = float(input())
    r = float(input())
    x = float(input())
    y = float(input())
    cal = math.sqrt((x-xm)**2 + (y-ym)**2)
    if cal <= r:
        print("Yes")
    else:
        print("No")
main()
