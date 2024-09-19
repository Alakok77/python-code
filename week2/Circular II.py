"""mod doc"""
import math
def main():
    """doc"""
    xm = float(input())
    ym =  float(input())
    rm = float(input())
    x = float(input())
    y = float(input())
    r = float(input())
    cal1 = math.sqrt((x - xm)**2 + (y - ym)**2)
    dis = rm + r
    # print(cal1)
    # print(dis)
    if cal1 < dis:
        print("Yes")
    else:
        print("No")
main()
