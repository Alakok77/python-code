"""mod doc"""
import math
def main():
    """doc"""
    r_var = float(input())
    a_var = float(input())
    b_var = float(input())
    circle = 2 * math.pi * r_var
    rectangle = (a_var * 2) + (b_var * 2)
    diff = abs(circle - rectangle)
    if circle > rectangle:
        print("Circle is longer")
    elif rectangle > circle:
        print("Rectangle is longer")
    else:
        print("Equal")
    print(f"{diff:.5f}")
main()
