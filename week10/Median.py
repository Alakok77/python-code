"""mod doc"""
import math
def main():
    """doc"""
    n_var = int(input())
    lst = []
    number = 0
    for _ in range(n_var):
        number = float(input())
        lst.append(number)
    lst.sort()
    point = ((n_var+1)/2) - 1
    if n_var%2:
        print(f"{lst[int(point)]:.3f}")
    else:
        print(f"{(lst[math.floor(point)] + lst[math.ceil(point)])/2:.3f}")
main()
