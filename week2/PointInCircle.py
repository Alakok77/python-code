"""PointInCircle"""
import math
def main():
    """PointInCircle"""
    x = int(input())
    y = int(input())
    r = int(input())
    xn = int(input())
    yn = int(input())
    cal = math.sqrt((xn-x)**2 + (yn-y)**2)
    if cal<=r :
        print("True")
    else:
        print("False")
main()
