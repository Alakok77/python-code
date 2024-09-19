"""mod doc"""
import math
def main():
    """doc"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    acount = int(input())
    bcount = int(input())
    ccount = int(input())
    dcount = int(input())
    most = 0
    if most < a/acount:
        most = a/acount
    if most < b/bcount:
        most = b/bcount
    if most < c/dcount:
        most = c/dcount
    if most < d/ccount:
        most = d/ccount
    print(math.ceil(most))
main()
