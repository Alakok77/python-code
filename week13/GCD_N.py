"""mod doc"""
import math
def main():
    """doc"""
    time = int(input())
    numbers = []
    for _ in range(time):
        numbers.append(int(input()))
    print(math.gcd(*numbers))
main()
