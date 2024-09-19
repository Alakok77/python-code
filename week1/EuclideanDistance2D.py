"""mod ddoc"""
import math
def main():
    """doc"""
    q1_var = float(input())
    q2_var = float(input())
    p1_var = float(input())
    p2_var = float(input())
    cal = math.sqrt(((q1_var - p1_var)**2) + ((q2_var - p2_var)**2))
    print(cal)
main()
